class Book:
    def __init__(self, name, last_update, creation_date, recipes_list):
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = recipes_list

    def get_recipe_by_name(self, name):
        """
        Print a recipe with the name `name` and return the instance
        """
        
        if not name or not isinstance(name, str):
            raise ValueError("Name should be a string")

        for recipe in self.recipes_list:
            if recipe.name.lower() == name.lower():
                return recipe
        return None

    def get_recipes_by_types(self, recipe_type):
        """
        Get all recipe names for a given recipe_type
        """
        
        if not recipe_type or not isinstance(recipe_type, str):
            raise ValueError("Recipe_type should be a string")
        
        matching_recipes = []
        for recipe in self.recipes_list:
            if recipe.recipe_type.lower() == recipe_type.lower():
                matching_recipes.append(recipe)

        return matching_recipes

    def add_recipe(self, recipe):
        """
        Add a recipe to the book and update last_update
        """
        
        self.recipes_list.append(recipe)

    def __str__(self):
        """
        Return the string to print with the recipe info
        """
        
        txt = f"Recipe for {self.name}:\n"
        txt += f"Last update: {self.last_update}\n"
        txt += f"Creation date: {self.creation_date}\n"
        txt += f"Recipes: "

        for recipe in self.recipes_list:
            txt += str(recipe.name)
            txt += ", "

        return txt