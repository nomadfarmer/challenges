"""
Advent of Code Day 02
Part one:

Take a list of strings. Find the count of strings which contain one (or
more) letters repeated exactly twice. Also count the strings which 
contain a letter repeated exactly three times. Return the product of
those two numbers.

Part two:

Find two ids that are identical except for one char in the same position.
e.g.: abcde and abide.
Return the chars that those two strings have in common (e.g. abde)

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
    with open("day02input") as f:
        box_ids = f.read().splitlines()

    for pair in itertools.combinations(box_ids, 2):
        diff_loc = -1
        for i in range(len(pair[0])):
            if pair[0][i] != pair[1][i]:
                if diff_loc >= 0:
                    # these chars are different but we already found
                    # different chars, so set diff_loc to an invalid
                    # value.
                    diff_loc = -1
                    break
                else:
                    diff_loc = i

        if diff_loc >= 0:
            print(pair[0][0:diff_loc] + pair[0][diff_loc+1:])


if __name__ == "__main__":
    part_b()
