class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
    
    def __str__(self):
        """Return the string to print with the recipe info"""
        
        txt = f"\nRecipe for {self.name}:\n"
        txt += f"Level: {self.cooking_lvl}\n"
        txt += f"Cooking time: {self.cooking_time} minutes\n"
        txt += f"Ingredients: {self.ingredients}\n"
        txt += f"Description: {self.description}\n"
        txt += f"Recipe type: {self.recipe_type}"
        return txt
