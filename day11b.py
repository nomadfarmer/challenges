#/usr/bin/env python3
"""
Advent of Code 2018 - Day 11 - 
https://adventofcode.com/2018/day/11

Umm... complicated hash?

rack_id = x + 10
power = rack_id * y 
     += serial (3628)
     *= rack_id
     Keep only the hundreds digit
     -= 5


"""

def power_level(x, y, serial):
    rack_id = x + 10
    power = (rack_id * y + serial) * rack_id
    power = int(str(power // 100)[-1]) - 5
    return power


def main():
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

    best_loc = (1, 1, 1)
    largest = -100000
    for size in range(1, 301):
        for x in range(1, 301 - size):
            for y in range(1, 301 - size):
                fuel_here = 0
                for i in range(size):
                    for j in range(size):
                        fuel_here += grid[x + i][y + j]
                if fuel_here > largest:
                    largest = fuel_here
                    best_loc = (x, y, size)
    print(f"Best location is at {best_loc}. Power: {largest}")



if __name__ == '__main__':
    main()
