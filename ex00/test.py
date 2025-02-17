from book import Book
from recipe import Recipe

# Main
if __name__ == "__main__" :
    tourte = Recipe("Tourte", 3, 60, ["pomme", "poire", "pêche"], "Une tourte aux fruits", "dessert")
    to_print = str(tourte)
    print(to_print)

    print("\n\n === Book ===")
    pizza = Recipe("Pizza", 2, 30, ["tomato", "cheese", "dough"], "Delicious pizza", "main")
    cake = Recipe("Cake", 1, 45, ["flour", "sugar", "butter"], "Sweet cake", "dessert")

    # Create a RecipeBook and add recipes
    book = Book("Cookbook", "2025-01-01", "2025-02-17", [])
    book.add_recipe(tourte)
    book.add_recipe(pizza)
    book.add_recipe(cake)
    print(book)

    # Get a recipe by name
    recipe = book.get_recipe_by_name("Pizza")

    recipe = book.get_recipe_by_name("Fish")

    # Get recipes by type
    main_recipes = book.get_recipes_by_types("dessert")
    print("\nDessert Recipes:")
    for main in main_recipes:
        print(main)