from book import Book
from recipe import Recipe

# Main
if __name__ == "__main__" :
    try:
        tourte = Recipe("Tourte", 3, 60, ["pomme", "poire", "pêche"], "Une tourte aux fruits", "dessert")
        to_print = str(tourte)
        print(to_print)

        print("\n\n ===== Book =====")
        pizza = Recipe("Pizza", 2, 30, ["tomato", "cheese", "dough"], "Delicious pizza", "lunch")
        cake = Recipe("Cake", 1, 45, ["flour", "sugar", "butter"], "Sweet cake", "dessert")

        # Create a RecipeBook and add recipes
        book = Book("Cookbook", "2025-01-01", "2025-02-17", [])
        book.add_recipe(tourte)
        book.add_recipe(pizza)
        book.add_recipe(cake)
        print(book)

        # Get a recipe by name
        recipe = book.get_recipe_by_name("Pizza")
        if recipe:
            print(f"\n-> Recipe found for Pizza: {recipe}")
        else:
            print("\n-> Recipe not found for Pizza")

        recipe = book.get_recipe_by_name("Fish")
        if recipe:
            print(f"\n-> Recipe found for Fish: {recipe}")
        else:
            print("\n-> Recipe not found for Fish")

        # Get recipes by type
        print("\n===== Dessert Recipes ======")

        dessert_recipes = book.get_recipes_by_types("dessert")
        for dessert in dessert_recipes:
            print(dessert)

    except ValueError as e:
        print(e)

    # Invalid recipe

    try:
        print("\n====== Invalid Recipe name ======")
        invalid_recipe = Recipe("", 3, 60, "pomme", "Une tourte aux fruits", "dessert")
    
    except ValueError as e:
        print(e)
    
    try:
        print ("\n====== Invalid Ingredients ======")
        invalid_recipe = Recipe("Invalid", 3, 60, "pomme", "Une tourte aux fruits", "dessert")
    
    except ValueError as e:
        print(e)

    try:
        print("\n====== Invalid Cooking Level ======")
        invalid_recipe = Recipe("Tourte", 6, 60, ["pomme", "poire", "pêche"], "Une tourte aux fruits", "dessert")
    except ValueError as e:
        print(e)

    try:
        print("\n====== Invalid Cooking Time ======")
        invalid_recipe = Recipe("Tourte", 3, -60, ["pomme", "poire", "pêche"], "Une tourte aux fruits", "dessert")
    except ValueError as e:
        print(e)
    
    try:
        print("\n====== Invalid Recipe Type ======")
        invalid_recipe = Recipe("Tourte", 3, 60, ["pomme", "poire", "pêche"], "Une tourte aux fruits", "dinner")
    except ValueError as e:
        print(e)