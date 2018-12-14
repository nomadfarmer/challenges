#!/usr/bin/env python3
"""
Advent of Code 2018 - Day  - Chocolate Charts
https://adventofcode.com/2018/day/14

"""


def recipe_pattern(pat):
    recipes = "37"
    elves = []
    pat = str(pat)
    for i in range(2):
        elves.append(i)
    while len(recipes) < len(pat) + 4 or pat not in recipes[-10:]:
        new_recipes = str(int(recipes[elves[0]]) + int(recipes[elves[1]]))
        recipes += new_recipes
        # print(recipes)
        for i in range(len(elves)):
            # print('len', len(recipes))
            elves[i] += (int(recipes[elves[i]]) + 1)
            elves[i] %= len(recipes)
            # print(elves[i])
    # print(recipes[-20:])
    # print(len(recipes))
    return recipes.rfind(pat)


assert recipe_pattern("51589") == 9
assert recipe_pattern("01245") == 5
assert recipe_pattern("92510") == 18
assert recipe_pattern("59414") == 2018

# print(recipe_pattern("290431"))
print(recipe_pattern("760221"))
