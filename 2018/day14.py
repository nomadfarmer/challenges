#!/usr/bin/env python3
"""
Advent of Code 2018 - Day  -
https://adventofcode.com/2018/day/

"""

from tqdm import tqdm
# import numpy as np
# import re
# import collections
# import sys
saved_recipes = [3, 7]


def next_recipe_scores(num):
    recipes = saved_recipes[:]
    elves = []
    for i in range(2):
        elves.append(i)
    while len(recipes) < num + 10:
        # combine recipes
        
        new_recipes = [int(x) for x in str(recipes[elves[0]] + recipes[elves[1]])]
        recipes += new_recipes
        # print(''.join(str(x) for x in recipes))
        for i in range(len(elves)):
            # print('len', len(recipes))
            elves[i] += (recipes[elves[i]] + 1)
            elves[i] %= len(recipes)
            # print(elves[i])
    recipe_string = ''.join(str(x) for x in recipes)
    print(recipe_string)
    print(recipe_string[num:num+10], 'len', len(recipe_string))
    return recipe_string[num:num+10]
        

# print('9', next_recipe_scores(9))
# print('5', next_recipe_scores(5))
# print('18', next_recipe_scores(18))

assert next_recipe_scores(9) == "5158916779"
assert next_recipe_scores(5) == "0124515891"
assert next_recipe_scores(18) == "9251071085"
assert next_recipe_scores(2018) == "5941429882"
print(next_recipe_scores(760221))
