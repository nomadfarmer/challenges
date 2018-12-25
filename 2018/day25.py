#!/usr/bin/env python3
"""
Advent of Code 2018 - Day 25 - Four-Dimensional Adventure
https://adventofcode.com/2018/day/25

4d geometry!

"""

import sys

fn = sys.argv[1] if len(sys.argv) > 1 else "input/day25"


class Universe:
    def __init__(self, fn):
        self.constellations = set()
        self.points = set()

        with open(fn) as f:
            raw_data = f.read().splitlines()

        for l in raw_data:
            new_p = Point(l)
            for c in self.constellations:
                c.try_add(new_p)
            if len(new_p.constellations) == 0:
                self.constellations.add(Constellation(new_p))
            elif len(new_p.constellations) > 1:
                self.merge_constellations(new_p.constellations.copy())

    def merge_constellations(self, cons):
        keep_con = cons.pop()
        for c in cons:
            keep_con.points |= c.points
            for p in c.points:
                p.constellations |= {keep_con}
                if c in p.constellations:
                    p.constellations.remove(c)
            self.constellations.remove(c)

    def count_constellations(self):
        return len([c for c in self.constellations if len(c.points) > 1])


class Constellation:
    def __init__(self, p):
        self.points = {p}
        p.constellations.add(self)

    def try_add(self, new_p):
        for p in self.points:
            if new_p.distance(p) <= 3:
                self.points.add(new_p)
                new_p.constellations.add(self)
                return True
        return False


class Point:
    def __init__(self, s):
        self.x, self.y, self.z, self.t = [int(i) for i in s.split(',')]
        self.constellations = set()

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) \
            + abs(self.z - other.z) + abs(self.t - other.t)


universe = Universe(fn)
print('Constellations: ', universe.count_constellations())
print('Including singles:', len(universe.constellations))
