"""
Advent of Code Day 02
Part one:

Take a list of strings. Find the count of strings which contain one (or
more) letters repeated exactly twice. Also count the strings which 
contain a letter repeated exactly three times. Return the product of
those two numbers.

"""

import itertools

def part_a():
    with open("day02input") as f:
        box_ids = f.read().splitlines()

    doubles = 0
    triples = 0

    for id in box_ids:
        found_double = False
        found_triple = False
        for c in id:
            if not found_double and id.count(c) == 2:
                found_double = True
            if not found_triple and id.count(c) == 3:
                found_triple = True
        if found_double:
            doubles += 1
        if found_triple:
            triples += 1

    print(doubles * triples)
     

def part_b():
    pass


if __name__ == "__main__":
    part_a()
