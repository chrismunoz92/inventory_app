from ingredient import Ingredient
from helpers import *

 
if __name__ == "__main__":
    ingredientName = 'Wax'
    ingredientUnitType = 'pound'
    ingredientQuantity = 4

    weight = createWeightObject(ingredientQuantity, ingredientUnitType)
    ing1 = Ingredient(ingredientName, weight.value, weight.unit)
    print(ing1)