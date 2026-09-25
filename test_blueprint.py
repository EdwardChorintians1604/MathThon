import sys
sys.path.insert(0, 'e:/MathThon')

print("Testing AI Blueprint Import...")
print("="*80)

try:
    from Back_End.routes.ai_routes import ai_bp
    print("✅ Blueprint imported successfully!")
    print(f"   Blueprint name: {ai_bp.name}")
    print(f"   Blueprint URL prefix: {ai_bp.url_prefix}")
    print(f"\n   Registered routes:")
    for rule in ai_bp.url_map.iter_rules() if hasattr(ai_bp, 'url_map') else []:
        print(f"     {rule.methods} -> {rule.rule}")
except ImportError as e:
    print(f"❌ Import Error: {e}")
except Exception as e:
    print(f"❌ Error: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()

print("="*80)
