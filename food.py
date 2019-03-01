__author__ = 'IAV'
__author__ = 'SBP'
"""
A module that represents the valid food types.

Author: Sean Strout @ RITCS
Author: Indrajeet Vidhate
Author: Shubham Patil
"""

# The set of valid food items
FOODS = {'beef', 'pork', 'chicken', 'onion', 'pepper', 'tomato', 'mushroom'}

# The set vegetables
VEGGIES = {'onion', "pepper", 'tomato', 'mushroom'}

# The calories for each food item (a dictionary, where 
# key = food name (string) and value = calories (int)
CALORIES = {
    'beef': 200,
    'chicken': 140,
    'pork': 100,
    'onion': 30,
    'pepper': 25,
    'tomato': 10,
    'mushroom': 7
}


# Implement Food class here
class Food:
    __slots__ = ['name', 'is_veggie', 'calories']

    def __init__(self, name):
        """
        This constructor accepts the name of food object
        and assigns is_veggie to True if it available
        in VEGGIES dictionary and assigns it's calorie
        value from the dictionary.
        """
        self.name = name
        if self.name in VEGGIES:
            self.is_veggie = True
        else:
            self.is_veggie = False
        self.calories = CALORIES[self.name]
