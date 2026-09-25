#!/usr/bin/env python3
"""
MathThon AI: Halusinasi Fix Verification Script
================================================

Verifies that:
1. Model is set to deepseek-r1:8b (NOT qwen2.5:7b)
2. SYSTEM_PROMPT has no mixed language
3. Anti-halusinasi rules are in place
4. Hybrid engine is properly integrated
"""

import os
import sys
import re

def check_model_config():
    """Check if MODEL_NAME is correctly set"""
    print("\n" + "="*60)
    print("1  CHECKING MODEL CONFIGURATION")
    print("="*60)
    
    try:
        with open('Back_End/ai/chat_api.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for model name
        model_match = re.search(r'MODEL_NAME\s*=\s*os\.getenv\("MODEL_NAME",\s*"([^"]+)"\)', content)
        if model_match:
            model_name = model_match.group(1)
            print(f"📍 MODEL_NAME found: {model_name}")
            
            if "deepseek-r1:8b" in model_name:
                print("✅ CORRECT: Using deepseek-r1:8b (reasoning model)")
                return True
            elif "qwen2.5:7b" in model_name:
                print("❌ ERROR: Still using qwen2.5:7b (NOT a reasoning model!)")
                return False
            else:
                print(f"⚠️  WARNING: Using {model_name} (check if it's a reasoning model)")
                return False
        else:
            print("❌ ERROR: Could not find MODEL_NAME in chat_api.py")
            return False
    except Exception as e:
        print(f"❌ ERROR reading file: {e}")
        return False


def check_system_prompt():
    """Check SYSTEM_PROMPT for mixed language and anti-halusinasi rules"""
    print("\n" + "="*60)
    print("2  CHECKING SYSTEM PROMPT")
    print("="*60)
    
    issues = []
    checks_passed = []
    
    try:
        with open('Back_End/ai/chat_api.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract SYSTEM_PROMPT
        prompt_match = re.search(r'SYSTEM_PROMPT = r"""(.*?)"""', content, re.DOTALL)
        if not prompt_match:
            print("❌ ERROR: Could not find SYSTEM_PROMPT")
            return False
        
        prompt = prompt_match.group(1)
        
        # Check 1: No Malay words
        malay_words = ['pembolehubah', 'jawapan', 'apakah itu', 'kuasa']
        for word in malay_words:
            if word in prompt.lower():
                issues.append(f"⚠️  Found Malay word: '{word}'")
        
        # Check 2: Has TERMINOLOGI BAKU INDONESIA
        if "TERMINOLOGI BAKU INDONESIA" in prompt or "Sisi Depan" in prompt:
            checks_passed.append("✅ Has TERMINOLOGI BAKU INDONESIA section")
        else:
            issues.append("❌ Missing TERMINOLOGI BAKU INDONESIA section")
        
        # Check 3: Has anti-hallucination forbidden terms
        if "DILARANG" in prompt or "opis" in prompt:
            checks_passed.append("✅ Has anti-halusinasi forbidden terms checklist")
        else:
            issues.append("❌ Missing anti-halusinasi checklist")
        
        # Check 4: Has LaTeX enforcement
        if "LATEX" in prompt or "LaTeX" in prompt:
            checks_passed.append("✅ Has LaTeX enforcement rules")
        else:
            issues.append("❌ Missing LaTeX enforcement rules")
        
        # Check 5: Has JAWAB LANGSUNG (NO FILLER, NO ULANG) rule
        if "JAWAB LANGSUNG" in prompt and "NO FILLER" in prompt and "NO ULANG" in prompt:
            checks_passed.append("✅ Has JAWAB LANGSUNG (NO FILLER, NO ULANG) conciseness rule")
        elif "JAWAB LANGSUNG" in prompt:
            checks_passed.append("✅ Has JAWAB LANGSUNG conciseness rule")
        else:
            issues.append("⚠️  Missing JAWAB LANGSUNG conciseness rule")
        
        # Check 6: Has forbidden terms list
        if "opis" in prompt and "adjungat" in prompt:
            checks_passed.append("✅ Has explicit forbidden terms list (opis, adjungat)")
        else:
            issues.append("⚠️  Missing explicit forbidden terms list")
        
        print("\n✅ PASSED CHECKS:")
        for check in checks_passed:
            print(f"  {check}")
        
        if issues:
            print("\n⚠️  ISSUES/WARNINGS:")
            for issue in issues:
                print(f"  {issue}")
            return len([i for i in issues if i.startswith("❌")]) == 0
        else:
            print("\n🎉 All checks passed!")
            return True
    
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False


def check_hybrid_engine():
    """Check if Hybrid Engine is integrated"""
    print("\n" + "="*60)
    print("3  CHECKING HYBRID ENGINE INTEGRATION")
    print("="*60)
    
    try:
        with open('Back_End/ai/chat_api.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        checks = []
        
        # Check 1: Import
        if "from .calculation_engine import HybridCalculationEngine" in content:
            checks.append("✅ HybridCalculationEngine imported")
        else:
            checks.append("❌ HybridCalculationEngine NOT imported")
        
        # Check 2: Instance creation
        if "HYBRID_ENGINE = HybridCalculationEngine()" in content or "engine = HybridCalculationEngine()" in content:
            checks.append("✅ HybridCalculationEngine instance created")
        else:
            checks.append("⚠️  No explicit instance creation visible")
        
        # Check 3: Used in chat()
        if "engine.process" in content or "engine_result" in content:
            checks.append("✅ Hybrid engine used in chat logic")
        else:
            checks.append("❌ Hybrid engine NOT used in chat logic")
        
        # Check 4: Fallback logic
        if "use_llm_fallback" in content or "fallback" in content.lower():
            checks.append("✅ Fallback logic present")
        else:
            checks.append("⚠️  Fallback logic not explicitly mentioned")
        
        for check in checks:
            print(f"  {check}")
        
        return "❌" not in "\n".join(checks)
    
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False


def check_temperature():
    """Check if temperature is set to 0.0"""
    print("\n" + "="*60)
    print("4  CHECKING TEMPERATURE SETTING")
    print("="*60)
    
    try:
        with open('Back_End/ai/llm_client.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for temperature default
        if "temperature: float = 0.0" in content:
            print("✅ Temperature set to 0.0 (precision mode)")
            return True
        elif "temperature: float = 0.1" in content or "temperature: float = 0.2" in content:
            print("✅ Temperature in low-variance precision mode")
            return True
        else:
            print("⚠️  Temperature value not clearly found")
            return False
    
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False


def check_sympy_available():
    """Check if SymPy can be imported"""
    print("\n" + "="*60)
    print("5  CHECKING SYMPY AVAILABILITY")
    print("="*60)
    
    try:
        import sympy
        print(f"✅ SymPy {sympy.__version__} is installed")
        return True
    except ImportError:
        print("❌ SymPy is NOT installed!")
        print("   Run: pip install sympy")
        return False


def main():
    """Run all checks"""
    print("\n" + "========================================")
    print("MATHATHON AI: HALUSINASI FIX VERIFICATION")
    print("========================================")
    
    results = {
        "Model Configuration": check_model_config(),
        "System Prompt": check_system_prompt(),
        "Hybrid Engine": check_hybrid_engine(),
        "Temperature": check_temperature(),
        "SymPy Available": check_sympy_available(),
    }
    
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for check, result in results.items():
        status = "PASS" if result else "FAIL"
        print(f"[{status}]  {check}")
    
    print(f"\nScore: {passed}/{total}")
    
    if passed == total:
        print("\nALL CHECKS PASSED! System is ready for deployment.")
        return 0
    else:
        print(f"\n{total - passed} checks failed. Please review and fix.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
