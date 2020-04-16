#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    # look through keys in recipe
    for rec_key, rec_value in recipe.items():
        print(f'recipe {rec_key,rec_value}')
    for ing_key, ing_value in ingredients.items():
        print(f'ing {ing_key,ing_value}')
        if ing_key != rec_key:
            return 0
    # search 1 by 1 by key in recipe to see if key is in ingredients
        # if there's a key in recipe thats not in ingredients, stop
    # if there's a key that matches, check to see if recipe value is higher
        # if its lower, stop, no batches can be made
        # if it's higher, divide the ingredients value by recipe value

recipe = { 'milk': 100, 'butter': 50, 'flour': 5, 'sugar': 20 }
ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }

recipe_batches(recipe, ingredients)
if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
