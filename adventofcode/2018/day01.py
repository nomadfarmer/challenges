#!/usr/bin/env python3
"""Advent of Code Day 01 part A:

The input file consists of lines of numbers with a sign. Our job is to
find the sum of the entire list of numbers.

Part B:
"""


def part_a():
    freq = 0
    f = open("input/day01")
    for line in f:
        freq += int(line)

    print(freq)


def part_b():
    freq = 0
    freq_history = {0}

    freq_changes = []
    f = open("input/day01")
    freq_changes = f.readlines()
    # freq_changes = [-6, +3, +8, +5, -6]
    # freq_changes = ['+1\n', '-2\n', '+3\n', '+1\n']
    # freq_changes = [+1, -1]
    # freq_changes = [7, 7, -2, -7, -4]

    found_it = False

    while not found_it:
        for change in freq_changes:
            freq += int(change)
            if freq in freq_history:
                found_it = True
                break
            else:
                freq_history.add(freq)

    print(freq)


if __name__ == "__main__":
    part_a()
    part_b()
