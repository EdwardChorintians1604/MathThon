from Back_End.__init__ import create_app

if __name__ == "__main__":
    app = create_app()
    print("\n" + "="*80)
    print("REGISTERED ROUTES:")
    print("="*80)
    
    # Filter hanya routes yang mengandung 'api/ai'
    ai_routes = [rule for rule in app.url_map.iter_rules() if 'api/ai' in rule.rule]
    
    if ai_routes:
        print("\nAI API Routes found:")
        for rule in ai_routes:
            print(f"  {rule.methods} -> {rule.rule}")
    else:
        print("\n⚠️  NO AI API ROUTES FOUND!")
        print("\nAll routes containing 'api':")
        api_routes = [rule for rule in app.url_map.iter_rules() if 'api' in rule.rule]
        for rule in api_routes:
            print(f"  {rule.methods} -> {rule.rule}")
    
    print("\n" + "="*80)
