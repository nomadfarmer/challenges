#!/usr/bin/env python3
"""
Advent of Code 2018 - Day 10 - The Stars Align
https://adventofcode.com/2018/day/10

Take a list of moving points and determine what message they will
eventually spell
"""

import re
from operator import itemgetter


class Stars:
    points = []

    def __init__(self, raw_data):
        for l in raw_data:
            m = re.search(r"(-?\d+).*?(-?\d+).*?(-?\d+).*?(-?\d+)", l)
            self.points.append(list(map(int, m.groups())))
        print(len(self.points))

    def tick(self, time):
        for p in self.points:
            p[0] += p[2] * time
            p[1] += p[3] * time

    def resolution(self):
        get_x = itemgetter(0)
        get_y = itemgetter(1)

        min_x = min(map(get_x, self.points))
        min_y = min(map(get_y, self.points))
        max_x = max(map(get_x, self.points))
        max_y = max(map(get_y, self.points))

        return ((max_x - min_x), (max_y - min_y), min_x, min_y)

    def display(self):
        x, y, mx, my = self.resolution()

        screen = []
        for i in range(y+1):
            screen.append([' ' for j in range(x + 1)])

        for x, y, dx, dy in self.points:
            screen[y - my][x - mx] = '#'

        for y in screen:
            print("".join(y))


def main():
    with open("tree_out") as f:
        raw_data = f.read().splitlines()
    stars = Stars(raw_data)

    time = 0
    granularity = (1000, 100, 10, 1)
    last_width, last_height, *_ = stars.resolution()
    this_height = last_height
    for g in granularity:
        while this_height <= last_height:
            last_height = this_height
            stars.tick(g)
            time += g
            this_width, this_height, *_ = stars.resolution()
        stars.tick(-g * 2)
        time -= g * 2
        last_width, last_height, *_ = stars.resolution()
        this_height = last_height

    stars.tick(1)

    print(time)
    stars.display()

    # stars.tick(10825)
    # time = 10825
    # while True:
    #     stars.display()
    #     print(time)
    #     input()
    #     stars.tick(1)
    #     time += 1


if __name__ == '__main__':
    main()
