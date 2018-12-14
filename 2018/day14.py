#!/usr/bin/env python3
"""
Advent of Code 2018 - Day  - Chocolate Charts
https://adventofcode.com/2018/day/14

"""


def next_recipe_scores(num):
    recipes = [3, 7]
    elves = []
    for i in range(2):
        elves.append(i)
    while len(recipes) < num + 10:
        new_recipes = [
            int(x) for x in str(recipes[elves[0]] + recipes[elves[1]])
        ]
        recipes += new_recipes
        # print(''.join(str(x) for x in recipes))
        for i in range(len(elves)):
            # print('len', len(recipes))
            elves[i] += (recipes[elves[i]] + 1)
            elves[i] %= len(recipes)
            # print(elves[i])
    recipe_string = ''.join(str(x) for x in recipes)
    print(recipe_string)
    print(recipe_string[num:num + 10], 'len', len(recipe_string))
    return recipe_string[num:num + 10]


assert next_recipe_scores(9) == "5158916779"
assert next_recipe_scores(5) == "0124515891"
assert next_recipe_scores(18) == "9251071085"
assert next_recipe_scores(2018) == "5941429882"
print(next_recipe_scores(760221))
