from ingredient import Ingredient

class Recipe:
    """A recipe object"""

    def __init__(self, name: str = None, ingredients: list[Ingredient] = None):
        self.name = name
        self.ingredients = ingredients

#TODO: Add function to store recipes
#TODO: Add function to calculate recipe quantities from raw ingredients