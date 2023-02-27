from ingredient import Ingredient
from recipe import Recipe
from helpers import *
 
if __name__ == '__main__':

    storageFile = './storage.csv'
    if not os.path.isfile(storageFile):
        open(storageFile,'x')

    recipeFile = './recipes.csv'
    if not os.path.isfile(recipeFile):
        open(recipeFile,'x')

    continueIngredients = input("Add ingredient? Y/n: ")
    while continueIngredients == 'y':
        storeIngredients()
        continueIngredients = input("Add ingredient? Y/n: ")
    
    file = open(storageFile,'a')

    for ingredient in ingredients:
        print(ingredient)
        file.write(f"{ingredient}\n")