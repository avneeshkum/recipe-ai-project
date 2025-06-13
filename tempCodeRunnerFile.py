  # 🛒 Shopping List
        print("\n🛒 Generating Shopping List...")
        shopping_list = generate_shopping_list(recipe)
        if shopping_list:
            print("\n🧾 Shopping List:")
            for item in shopping_list:
                print(f"- {item}")
        else:
            print("❌ No ingredients found for shopping list.")
