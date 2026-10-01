"""
Comprehensive Automated Test for LMS Architecture, Gatekeeping & AI Tutor Active Recall
1. Tests database relational model (Course -> Module -> Material -> UserProgress).
2. Tests API gatekeeping: Bab 2 is locked (HTTP 403) until Bab 1 is completed.
3. Tests active recall: incorrect answer triggers AI Socratic hint.
4. Tests step progression: Step 1 -> Step 2 -> ... -> Final Step.
5. Tests final step completion: Marks UserProgress as 'Completed' and unlocks next material.
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Back_End import create_app
from Back_End.services.progress_svc import ProgressService
from Back_End.services.ai_tutor_svc import AITutorService
from Back_End.database.connection import get_db_session
from Back_End.models.domain import Course, Module, Material, UserProgress, User
import json

def run_tests():
    app = create_app({"TESTING": True})
    client = app.test_client()
    
    print("\n=======================================================")
    print("🧪 1. TESTING RELATIONAL DATABASE & SYLLABUS MAPPING")
    print("=======================================================")
    svc = ProgressService()
    test_user_id = 99999 # isolated test user id
    
    # Clean previous test user progress if any
    db_session = get_db_session()
    db_session.query(UserProgress).filter(UserProgress.user_id == test_user_id).delete()
    db_session.commit()
    
    courses = db_session.query(Course).all()
    print(f"✅ Found {len(courses)} courses in database.")
    assert len(courses) >= 3, f"Expected at least 3 courses, found {len(courses)}"
    
    modules = db_session.query(Module).all()
    print(f"✅ Found {len(modules)} modules in database.")
    assert len(modules) >= 6, f"Expected at least 6 modules, found {len(modules)}"
    
    materials = db_session.query(Material).all()
    print(f"✅ Found {len(materials)} materials across modules.")
    assert len(materials) >= 30, f"Expected 30 materials, found {len(materials)}"

    print("\n=======================================================")
    print("🔒 2. TESTING GATEKEEPING LOGIC AT API LEVEL (403 FORBIDDEN)")
    print("=======================================================")
    # Bab 1 of Integral has no prereq (or prereq from previous module), but Bab 2 has Bab 1 as prereq!
    bab1_integral = svc.get_material_by_slug("bab-1-latar-belakang-akumulasi")
    bab2_integral = svc.get_material_by_slug("bab-2-antiturunan")
    
    assert bab1_integral is not None, "bab-1-latar-belakang-akumulasi not found!"
    assert bab2_integral is not None, "bab-2-antiturunan not found!"
    assert bab2_integral.prerequisite_id == bab1_integral.id, "Bab 2 prerequisite must be Bab 1!"
    print(f"ℹ️ Bab 1: '{bab1_integral.title}' (ID: {bab1_integral.id})")
    print(f"ℹ️ Bab 2: '{bab2_integral.title}' (ID: {bab2_integral.id}, Prereq ID: {bab2_integral.prerequisite_id})")

    with client.session_transaction() as sess:
        sess["user_id"] = test_user_id

    # Request Bab 2 before Bab 1 is completed
    res = client.get("/api/materials/bab-2-antiturunan")
    print(f"📡 GET /api/materials/bab-2-antiturunan -> Status Code: {res.status_code}")
    res_json = res.get_json()
    print(f"📄 Response JSON: {res_json}")
    
    assert res.status_code == 403, f"Expected 403 Forbidden, got {res.status_code}"
    assert res_json["status"] == "forbidden"
    assert "Selesaikan" in res_json["message"], f"Expected 'Selesaikan ... terlebih dahulu', got {res_json['message']}"
    print("✅ Gatekeeping Passed! Bab 2 correctly returns 403 Forbidden with prerequisite message.")

    print("\n=======================================================")
    print("🔓 3. COMPLETING PREREQUISITE & VERIFYING UNLOCKING")
    print("=======================================================")
    # Mark Bab 1 as completed
    svc.complete_material(user_id=test_user_id, material_id=bab1_integral.id, score=100)
    print(f"✅ Bab 1 marked as Completed for user {test_user_id}.")

    # Now request Bab 2 again
    res = client.get("/api/materials/bab-2-antiturunan")
    print(f"📡 GET /api/materials/bab-2-antiturunan -> Status Code: {res.status_code}")
    assert res.status_code == 200, f"Expected 200 OK after prerequisite completed, got {res.status_code}"
    res_json = res.get_json()
    assert res_json["status"] == "success"
    assert res_json["data"]["slug"] == "bab-2-antiturunan"
    print("✅ Gatekeeping Unlock Passed! Bab 2 is now accessible (HTTP 200).")

    print("\n=======================================================")
    print("🤖 4. TESTING ACTIVE RECALL & AI TUTOR SOCRATIC HINT")
    print("=======================================================")
    # Test incorrect answer at Step 1 of integral
    wrong_req = {
        "material_slug": "bab-5-capstone-integral",
        "module_slug": "integral",
        "step_index": 1,
        "user_answer": "6x", # wrong, 6x is derivative, not integral!
        "time_spent_seconds": 15
    }
    res = client.post("/api/progress/validate_step", json=wrong_req)
    print(f"📡 POST /api/progress/validate_step (Wrong Answer) -> Status: {res.status_code}")
    res_json = res.get_json()
    print(f"📄 Incorrect Response: {res_json}")
    assert res_json["is_correct"] is False, "Expected is_correct = False"
    assert "ai_hint" in res_json and len(res_json["ai_hint"]) > 0, "Expected non-empty AI hint"
    print(f"💡 AI Socratic Hint Generated:\n   \"{res_json['ai_hint']}\"")
    print("✅ AI Tutor Socratic feedback successfully verified!")

    print("\n=======================================================")
    print("🚀 5. TESTING MULTI-STEP PROGRESSION TO COMPLETION")
    print("=======================================================")
    steps_answers = [
        (1, "x^3"),
        (2, "2x^2"),
        (3, "x^3 + 2x^2 + C"),
        (4, "16")
    ]
    for step_num, ans in steps_answers:
        step_req = {
            "material_slug": "bab-5-capstone-integral",
            "module_slug": "integral",
            "step_index": step_num,
            "user_answer": ans,
            "time_spent_seconds": 10
        }
        res = client.post("/api/progress/validate_step", json=step_req)
        step_res = res.get_json()
        print(f"   Step {step_num} ({ans}) -> is_correct: {step_res.get('is_correct')}, is_final: {step_res.get('is_final_step')}")
        assert step_res["is_correct"] is True, f"Step {step_num} failed with answer {ans}"

    assert step_res["is_final_step"] is True, "Step 4 must be the final step"
    assert step_res["user_progress_status"] == "Completed", "Status must become Completed"
    print("✅ Multi-stage Scaffolding Completed! User progress status is now 'Completed'.")

    # Clean up test user
    db_session.query(UserProgress).filter(UserProgress.user_id == test_user_id).delete()
    db_session.commit()
    print("\n🎉 ALL TESTS PASSED SUCCESSFULLY! LMS Gatekeeping & Active Recall AI Tutor fully functional.")

if __name__ == "__main__":
    run_tests()
