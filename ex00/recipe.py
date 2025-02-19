def _is_valid_string(name):
    """
    Check if the string is not empty and contains only letters
    """

    if not name or not isinstance(name, str) or not name.isalpha():
        raise ValueError("Empty string or invalid name")
    return name


def _validate_cooking_lvl(cooking_lvl):
    """
    Check if the cooking level is between 1 and 5
    """

    if not _is_number_in_range(cooking_lvl, 1, 5):
        raise ValueError(f"'{cooking_lvl}', Cooking level must be a number between 1 and 5")
    return cooking_lvl


def _validate_cooking_time(cooking_time):
    """
    Check if the cooking time is a non-negative number
    """
    if not _is_number_in_range(cooking_time, 0, 2147483647):
        raise ValueError(f"'{cooking_time}', Cooking time must be a non-negative number")
    return cooking_time


def _is_number_in_range(value, min_val, max_val):
    """
    Check if the value is a number and is in the range [min_val, max_val]
    """
    if not isinstance(value, int):
        raise ValueError(f"'{value}', Invalid number")
    
    if not min_val <= value <= max_val:
        raise ValueError(f"'{value}', Number out of range")
    return value


def _is_valid_type(types):
    """
    Check if the type is valid (start, lunch, dessert)
    """

    valid_types = ["start", "lunch", "dessert"]
    if types not in valid_types:
        raise ValueError(f"'{types}', Invalid type: {valid_types}'")
    return types


def _validate_ingredients(ingredients):
    """
    Check if the ingredients are a list
    """
    if not isinstance(ingredients, list):
        raise ValueError("Ingredients must be a list")
    
    for ingredient in ingredients:
        _is_valid_string(ingredient)
    
    return ingredients


class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        # name
        self.name = _is_valid_string(name)
        # range from 1 to 5
        self.cooking_lvl = _validate_cooking_lvl(cooking_lvl)
        # in minutes (no negative numbers)
        self.cooking_time = _validate_cooking_time(cooking_time)
        # list of ingredients (represented string)
        self.ingredients = _validate_ingredients(ingredients)
        # description of the recipe (can be empty)
        self.description = description if description else "No description"
        # start, lunch, dessert
        self.recipe_type = _is_valid_type(recipe_type)

    def __str__(self) -> str:
        """Return the string to print with the recipe info"""
        
        txt = f"\nRecipe for {self.name}:\n"
        txt += f"Level: {self.cooking_lvl}\n"
        txt += f"Cooking time: {self.cooking_time} minutes\n"
        txt += f"Ingredients: {self.ingredients}\n"
        txt += f"Description: {self.description}\n"
        txt += f"Recipe type: {self.recipe_type}"
        return txt
