#!/usr/bin/env python3
"""
Advent of Code 2018 - Day 22 - Mode Maze
https://adventofcode.com/2018/day/22

"""

import numpy as np

# depth = 510
# target = (10, 10)

depth = 5913
target = (8, 701)

shape = (target[0] + 40, target[1] + 40)

geo_index = np.zeros(shape, dtype=int)
erosion = np.zeros(shape, dtype=int)
terrain = np.zeros(shape, dtype=int)

for x in range(shape[0]):
    for y in range(shape[1]):
        if (x, y) == (0, 0) or (x, y) == target:
            geo_index[x, y] = 0
        elif y == 0:
            geo_index[x, y] = x * 16807
        elif x == 0:
            geo_index[x, y] = y * 48271
        else:
            geo_index[x, y] = erosion[x - 1, y] * erosion[x, y - 1]
        erosion[x, y] = (geo_index[x, y] + depth) % 20183
        terrain[x, y] = erosion[x, y] % 3

print(terrain.transpose())

sum_of_min_rect = np.cumsum(
    np.cumsum(terrain, axis=0).transpose(), axis=0).transpose()[target]
print('Part 1:', sum_of_min_rect)

# tools: 0 = nothing, 1 = torch, 2 = climbing gear
# tool key can never equal terrain type.
tools = set(range(3))

# frontiers[(x, y, tool)] = time to get here
# steps: ditto
frontiers = {(0, 0, 1)}
steps = {(0, 0, 1): (0, '')}

while frontiers:
    old_front = frontiers.copy()
    frontiers = set()
    for (x, y, tool) in old_front:
        time, path = steps[(x, y, tool)]
        dirs = [(x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)]
        for (new_x, new_y) in dirs:
            if new_x not in range(shape[0]) or new_y not in range(shape[1]):
                continue

            new_time = time + 1

            if terrain[new_x, new_y] == tool:
                new_time += 7
                bad_tools = {terrain[x, y], terrain[new_x, new_y]}
                new_tool = (tools - bad_tools).pop()
                path += 's' + str(new_tool)
            elif (new_x, new_y) == target and tool != 1:
                print('switching to torch for final square')
                new_time += 7
                new_tool = 1
                path += 's1'
            else:
                new_tool = tool

            dir_names = {(0, -1): 'N', (1, 0): 'E', (0, 1): 'S', (-1, 0): 'W'}
            path += dir_names[(new_x - x, new_y - y)]

            if (new_x, new_y, new_tool) not in steps \
               or steps[(new_x, new_y, new_tool)][0] > new_time:

                steps[(new_x, new_y, new_tool)] = (new_time, path)
                frontiers.add((new_x, new_y, new_tool))

print(steps[target + (1, )])
