#!/usr/bin/env python3
"""
Advent of Code 2018 - Day  - 18
https://adventofcode.com/2018/day/18

Conway's game of life again?

open (.) -> Trees if 3 or more of (8) adjacent cells are trees.
trees (|) -> Lumberyard if 3 or more adj. cells are lumberyards.
lumberyard (#) -> Stays lumberyard only if adjacent to 1+ # and
                  1+ |. Otherwise, it becomes '.'

Output: trees * lumberyard after 10 rounds.
Part B: trees * lumberyard after 1_000_000_000 rounds.
"""

import sys
from copy import deepcopy

from termcolor import colored


def surrounding(l, coord):
    s_c = set(((-1, -1), (-1, 0), (-1, 1), (-1, 0), (1, 0),
               (1, -1), (1, 0), (1, 1), (0, 1), (0, -1)))
    x, y = coord
    neighbors = []
    for d in s_c:
        x_off, y_off = d
        if x + x_off < 0 or y + y_off < 0 \
           or y + y_off > len(l) - 1 or x + x_off > len(l[y]) - 1:
            continue
        else:
            neighbors.append(l[y + y_off][x + x_off])

    return neighbors


def print_map(field):
    print('\n')
    for y in field:
        line = ''.join(y)
        line = line.replace('.', colored('.', 'white'))
        line = line.replace('|', colored('|', 'green'))
        line = line.replace('#', colored('#', 'yellow'))
        print(line)


fn = sys.argv[1] if len(sys.argv) > 1 else "input/day18"
with open(fn) as f:
    raw_lines = f.read().splitlines()

trees = 0
yards = 0
field = []
for y in range(len(raw_lines)):
    field.append([])
    field[y] = list(raw_lines[y])
    trees += field[y].count('|')
    yards += field[y].count('#')

print_map(field)

scores = [trees * yards]
score_count = {scores[0]: 1}

for i in range(1, 1_000_000_001):
    new_field = [[[] for x in range(len(field[0]))] for y in range(len(field))]
    open_ = 0
    trees = 0
    yards = 0
    for y in range(len(field)):
        for x in range(len(field[y])):
            neighbors = surrounding(field, (x, y))
            if field[y][x] == '.':
                if neighbors.count('|') >= 3:
                    new_field[y][x] = '|'
                    trees += 1
                else:
                    new_field[y][x] = '.'
            elif field[y][x] == '|':
                if neighbors.count('#') >= 3:
                    new_field[y][x] = '#'
                    yards += 1
                else:
                    new_field[y][x] = '|'
                    trees += 1
            elif field[y][x] == '#':
                if neighbors.count('#') >= 1 and neighbors.count('|') >= 1:
                    new_field[y][x] = '#'
                    yards += 1
                else:
                    new_field[y][x] = '.'

    field = deepcopy(new_field)


    score = trees * yards
    scores.append(score)

    if i == 10:
        print_map(field)


    # I thought that scores.count would be inefficient, switched to a version
    # that used a dict... it wasn't any faster for this list size.
    if scores.count(score) >= 3:
        print_map(field)
        print('Cycle found by round', i)

        cycle = [0]
        for j in range(3):
            cycle.append(scores.index(score, cycle[-1] + 1))
        cycle_length = cycle[-1] - cycle[-2]
        left_to_1M = 1_000_000_000 - i
        mod = left_to_1M % cycle_length
        score_at_1M = scores[-(cycle_length - (mod - 1))]
        print('After 10 minutes, the score will be', scores[10])
        print('After 1M minutes, the score will be', score_at_1M)

        break
