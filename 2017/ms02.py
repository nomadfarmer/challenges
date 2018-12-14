#!/usr/bin/env python3
"""Advent of Code 2017 Day (ms) 02: Corruption Checksum
https://adventofcode.com/2017/day/2

Create a checksum for a matrix of numbers. The checksum for each line is the difference
between the largest and smallest value in the line. The checksum for the whole matrix
is the sum of each line's checksum.

E.G:
for the matrix: 
5 1 9 5
7 5 3
2 4 6 8

9 - 1 = 8
7 - 3 = 4
8 - 2 = 6
8 + 4 + 6 = 18

I put the test data and 'real' data in the files ms02_test and ms02_input

PART 2
==========
Instead of min and max, now each line's checksum is the result of dividing
the only two numbers on the line that are evenly divisible.
"""

import itertools


def test_ms02():
    assert ms02('ms02_test') == 18


def test_ms02_part2():
    assert ms02_part2('ms02_p2_test') == 9


def ms02(filename):
    f = open(filename)
    checksum = 0
    for line in f:
        line = line.split("\t")
        max_n = int(line[0])
        min_n = int(line[0])
        for i in line:
            if int(i) > max_n:
                max_n = int(i)
            if int(i) < min_n:
                min_n = int(i)
        checksum += max_n - min_n
    return checksum


def ms02_part2(filename):
    f = open(filename)
    checksum = 0
    for line in f:
        entries = line.split()
        entries = [int(i) for i in entries]
        # entries.sort(reverse = True)
        for pair in itertools.permutations(entries, 2):
            if pair[0] % pair[1] == 0:
                checksum += pair[0] // pair[1]
                break
    return checksum


def main():
    print(ms02("ms02_input"))
    print(ms02_part2("ms02_input"))


if __name__ == '__main__':
    main()
