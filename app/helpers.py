from measurement.measures import Weight
from measurement.utils import guess
from ingredient import *
import os

ingredients = []

def createWeightObject(quantity: int = None, type: str = None) -> Weight:
    weightTypes = ['attogram', 'centigram', 'decagram', 'decigram', 'exagram', 'femtogram', 'gigagram', 'gram', 'hectogram', 'kilogram', 'long ton', 'mcg', 'megagram', 'metric ton', 'metric tonne', 'microgram', 'milligram', 'nanogram', 'ounce', 'petagram', 'picogram', 'pound', 'short ton', 'teragram', 'ton', 'yoctogram', 'yottagram', 'zeptogram', 'zetagram']
    
    for types in weightTypes:
        if types == type.lower():

            # Creates Guess type object from user input with 0 volume 
            unit = guess(0, type)

            # Creates Weight object from Guess type
            weight = Weight(unit.unit)

            # Adds quantity from user input
            weight.value = weight.value + quantity

            return weight   

def storeIngredients():
        ingredientName = input("Ingredient name: ")
        ingredientUnitType = input("Unit type: ")
        ingredientQuantity = int(input("Quantity: "))

        weight = createWeightObject(ingredientQuantity, ingredientUnitType)
        ingredient = Ingredient(ingredientName, weight.value, weight.unit)

        ingredients.append(ingredient)
