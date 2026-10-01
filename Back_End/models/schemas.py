"""
Pydantic Schemas / Serializers
Validasi data input dan output untuk REST API endpoint.
"""
from pydantic import BaseModel, Field
from typing import Optional, List, Any
from datetime import datetime

# ==========================================
# 1. Active Recall & Step Validation Schemas
# ==========================================
class ValidateStepRequest(BaseModel):
    material_id: Optional[int] = Field(None, description="ID materi di database")
    material_slug: Optional[str] = Field(None, description="Slug materi (misal: bab-5-capstone-integral)")
    module_slug: Optional[str] = Field(None, description="Slug modul (misal: integral)")
    step_index: int = Field(..., ge=1, le=10, description="Tahap langkah active recall yang sedang dikerjakan")
    user_answer: str = Field(..., min_length=1, description="Jawaban yang diinputkan pengguna")
    time_spent_seconds: Optional[int] = Field(0, description="Waktu yang dihabiskan untuk tahap ini")

class ValidateStepResponse(BaseModel):
    is_correct: bool
    is_final_step: bool
    current_step: int
    next_step: Optional[int] = None
    feedback_message: str
    ai_hint: Optional[str] = None
    user_progress_status: str # Locked, In_Progress, Completed
    unlocked_next_material_id: Optional[int] = None
    unlocked_next_slug: Optional[str] = None

# ==========================================
# 2. Materials & Syllabus Schemas
# ==========================================
class MaterialItemSchema(BaseModel):
    id: int
    title: str
    slug: str
    chapter_number: int
    is_checkpoint: bool
    prerequisite_id: Optional[int] = None
    summary: Optional[str] = None
    status: str = "Locked" # Locked, In_Progress, Completed
    score: int = 0
    is_accessible: bool = False

class ModuleSyllabusSchema(BaseModel):
    id: int
    name: str
    slug: str
    description: Optional[str] = None
    order_index: int
    materials: List[MaterialItemSchema] = []
    completion_percentage: float = 0.0

class CourseSyllabusSchema(BaseModel):
    id: int
    title: str
    slug: str
    description: Optional[str] = None
    modules: List[ModuleSyllabusSchema] = []
    total_materials: int = 0
    completed_materials: int = 0

class MaterialContentResponse(BaseModel):
    id: int
    title: str
    slug: str
    module_name: str
    module_slug: str
    course_title: str
    chapter_number: int
    is_checkpoint: bool
    prerequisite_id: Optional[int] = None
    prerequisite_title: Optional[str] = None
    status: str
    content: Optional[str] = None
    summary: Optional[str] = None
    next_material_slug: Optional[str] = None

# ==========================================
# 3. Auth & User Schemas
# ==========================================
class UserLoginSchema(BaseModel):
    username_or_email: str
    password: str

class UserRegisterSchema(BaseModel):
    name: str
    username: str
    email: str
    password: str

class UserTokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user_id: int
    name: str
    username: str
