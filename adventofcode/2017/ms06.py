#!/usr/bin/env python3
"""
Advent of Code 2017 - Day 06 - Memory Reallocation
https://adventofcode.com/2017/day/6

Balance blocks in memory banks. The memory banks are a list containing
the number of blocks of memory in each bank. Balance the banks by taking
the blocks from the bank with the most blocks and redistributing them, 
mancala style (that is, one goes to each of the next banks until they
are all redistributed).

This will result in an infinite loop.

Our task is to ascertain how many redistributions happen before we see
a configuration we've seen before.

The second task is to see how long the actual loop is from that point.
"""


def reallocate(banks):
    history = []
    steps = 0
    while banks not in history:
        steps += 1
        history.append(banks[:])
        pointer = banks.index(max(banks))
        blocks = banks[pointer]
        banks[pointer] = 0
        for i in range(blocks):
            pointer = (pointer + 1) % len(banks)
            banks[pointer] += 1
    return steps


test_data = [0, 2, 7, 0]
assert reallocate(test_data) == 5
assert test_data == [2, 4, 1, 2]

with open("ms06input") as f:
    banks = list(map(int, f.read().split("\t")))

print("Steps for part 1:", reallocate(banks))
print("Current config:", banks)

print("Steps for part 2:", reallocate(banks))
print("End config:", banks)
