#!/usr/bin/env python3
"""
Advent of Code 2018 - Day  - 17
https://adventofcode.com/2018/day/17

"""

import sys
import re
<<<<<<< HEAD
=======
# import collections

# import numpy as np
# from tqdm import tqdm
>>>>>>> a878e57e57d2fbc1450aff60e88c8a24aa0a1f7d
from termcolor import colored


def flood(start, map_):
    # look down until we find water or clay
    # print('Flood called with', start)
    x = start[0]
    new_water = 0
    for y in range(start[1], len(map_)):
        if map_[y][x] == '.':
            map_[y][x] = '|'
            new_water += 1
        if y == len(map_) - 1 or map_[y + 1][x] in '#~':
            break
    if y == len(map_) - 1:  # and map_[y + 1][x] not in '#~':
        return (new_water, set())
    else:
        # fill left and right
        s, nw, nf = settle((x, y), map_)
<<<<<<< HEAD
=======
        # if s:
        #     nf.add(start)
>>>>>>> a878e57e57d2fbc1450aff60e88c8a24aa0a1f7d
        return (nw + new_water, nf)


def settle(start, map_):
    done = {-1: False, 1: False}
    layer = set()
    x, y = start
    new_floods = set()
    settled = True
    dont_count = set()
    for offset in range(0, len(map_[0])):
        for dire in [d for d in done.keys() if not done[d]]:
            this_x = x + dire * offset
            if this_x < 0 or this_x > len(map_[0]):
                done[dire] = True
            if map_[y][this_x] == '#':
                done[dire] = True
            elif map_[y + 1][this_x] == '.':
                settled = False
                new_floods.add((this_x, y))
                done[dire] = True
            elif map_[y + 1][this_x] == '|':
                settled = False
<<<<<<< HEAD
=======
                # Don't start new floods here, it should already be covered
>>>>>>> a878e57e57d2fbc1450aff60e88c8a24aa0a1f7d
                done[dire] = True
            else:
                if map_[y][this_x] in r'|~-':
                    dont_count.add((this_x, y))
                layer.add((this_x, y))
    fill = '~' if settled else '-'
    if settled:
        new_floods.add((x, y - 1))
    for c in layer:
        map_[c[1]][c[0]] = fill
<<<<<<< HEAD

=======
    # if settled and
    #    print( 'dc   ', dont_count,'\nl   ', layer, '\nl^dc', layer ^ dont_count)
>>>>>>> a878e57e57d2fbc1450aff60e88c8a24aa0a1f7d
    return (settled, len(layer ^ dont_count), new_floods)


def print_map(map_):
    print(3 * '\n')
    no_water_limit = 10
    for y in range(len(map_)):
        line = ''.join(map_[y])
        if '~' not in line and '|' not in line:
            no_water_limit -= 1
            if no_water_limit <= 0:
                break
        line = line[-100:]
        line = line.replace('.', colored('.', 'white'))
        line = line.replace('~', colored('~', 'blue'))
        line = line.replace('|', colored('|', 'blue'))
        line = line.replace('-', colored('-', 'blue'))
        line = line.replace('#', colored('#', 'yellow'))
        print(line, y)
    print()


fn = sys.argv[1] if len(sys.argv) > 1 else "input/day17_t"
with open(fn) as f:
    raw_data = f.read().splitlines()

map_ = []
x_max = y_max = -10**5
x_min = y_min = 10**5

clay = set()

for l in raw_data:
    info = re.findall(r'([xy]=[\d.]+)', l)
    coords = {}
    for value in info:
        var, values = value.split('=')
        coords[var] = [int(x) for x in values.split('..')]
    if coords['x'][0] < x_min:
        x_min = coords['x'][0]
    if coords['x'][-1] > x_max:
        x_max = coords['x'][-1]
    if coords['y'][0] < y_min:
        y_min = coords['y'][0]
    if coords['y'][-1] > y_max:
        y_max = coords['y'][-1]
    for x in range(coords['x'][0], coords['x'][-1] + 1):
        for y in range(coords['y'][0], coords['y'][-1] + 1):
            clay.add((x, y))

x_min -= 1
x_max += 1

map_ = [['.' for x in range(x_min, x_max + 1)] for y in range(0, y_max + 1)]

for c in clay:
    map_[c[1]][c[0] - x_min] = '#'

<<<<<<< HEAD
water, falls = flood((500 - x_min, y_min), map_)
while falls:
    new_falls = set()
    for c in falls:
        nw, nf = flood(c, map_)
        water += nw
        new_falls |= nf
    falls = new_falls

print(water)

water = 0
standing_water = 0
for y in map_:  # range(y_min, y_max + 1):
    # print(y)
    standing_water_here = y.count('~')
    standing_water += standing_water_here
    water += standing_water_here + y.count('-') + y.count('|')
    # print(water)
    # input()
print('All water:', water)
print('Standing water:', standing_water)
=======
print_map(map_)

water, falls = flood((500 - x_min, y_min), map_)
while falls:
    # print(falls)
    new_falls = set()
    for c in falls:
        # print_map(map_)
        # print(water, falls)
        nw, nf = flood(c, map_)
        water += nw
        # input()
        new_falls |= nf
    falls = new_falls

print_map(map_)
print(water)
water = 0
for y in map_:  # range(y_min, y_max + 1):
    # print(y)
    water += y.count('-') + y.count('|') + y.count('~')
    # print(water)
    # input()
print('All water:', water)

water = 0
for y in map_:  # range(y_min, y_max + 1):
    water += y.count('~')

print('Standing water:', water)
>>>>>>> a878e57e57d2fbc1450aff60e88c8a24aa0a1f7d
