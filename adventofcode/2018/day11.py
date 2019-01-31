# /usr/bin/env python3
"""
Advent of Code 2018 - Day 11 - 
https://adventofcode.com/2018/day/11

Populate a grid from our seed, then find the upper left corner of the
3x3 grid with the largest sum.
"""
import numpy as np
import itertools
from tqdm import tqdm


def power_level(x, y, serial=4455):
    # print("Power_level called")
    rack_id = x + 10
    power = (rack_id * y + serial) * rack_id
    power = ((power // 100) % 10) - 5
    return power


def sum_func(arr, size=3):
    return lambda x, y: arr[x: x + size, y: y + size].sum()


def new():
    grid = np.fromfunction(power_level, (301, 301), dtype=int)

    fuels = np.empty((301 - 3, 301 - 3), dtype=int)
    # for (x, y) in itertools.product(range(1, 298), repeat=2):
    for x in tqdm(range(1, 298)):
        for y in range(1, 298):
            fuels[x, y] = grid[x:x + 3, y:y + 3].sum()
    loc = fuels.argmax()
    print("{},{}".format(loc // (301-3), loc % (301-3)))


def third():
    grid = np.fromfunction(power_level, (301, 301), dtype=int)
    best_fuel = -10000
    for (x, y) in itertools.product(range(1, 298), repeat=2):
        fuel_here = grid[x:x + 3, y:y + 3].sum()
        if fuel_here > best_fuel:
            best_fuel = fuel_here
            best_loc = "{},{}".format(x, y)
    print(best_loc)


def old():
    serial = 3628
    assert power_level(122, 79, 57) == -5
    assert power_level(217, 196, 39) == 0
    assert power_level(101, 153, 71) == 4

    grid = [0] * 301
    for x in range(301):
        grid[x] = [0] * 301

    for x in range(1, 301):
        for y in range(1, 301):
            grid[x][y] = power_level(x, y, serial)

    best_loc = (1, 1)
    largest = -100000
    for x in range(1, 298):
        for y in range(1, 298):
            fuel_here = 0
            for i in range(3):
                for j in range(3):
                    fuel_here += grid[x + i][y + j]
            if fuel_here > largest:
                largest = fuel_here
                best_loc = (x, y)
    # print(f"Best location is at {best_loc}. Power: {largest}")


if __name__ == '__main__':
    new()
