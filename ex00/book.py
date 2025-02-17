class Book :
    def __init__ (self, name, last_update, creation_date, recipes_list) :
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = recipes_list

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for recipe in self.recipes_list:
            if recipe.name.lower() == name.lower():
                return recipe
        return None

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        filtered_recipes = [recipe for recipe in self.recipes_list if recipe.recipe_type.lower() == recipe_type.lower()]
        return filtered_recipes

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        self.recipes_list.append(recipe)

    def __str__(self):
        """Return the string to print with the recipe info"""
        
        txt = f"Recipe for {self.name}:\n"
        txt += f"Last update: {self.last_update}\n"
        txt += f"Creation date: {self.creation_date}\n"

        return txt