#!/usr/bin/env python3
"""
Advent of Code 2018 - Day 12 - Subterranean Sustainability
https://adventofcode.com/2018/day/12

One dimensional Conway's Game of Life.

Input is a string of #'s and .'s representing plants in rows of pots
along with a list of rules for which pots will have plants in the next
generation.

Each pot has a value (0, 1, 2 ... for the data we start with, but if 
plants grow to the left they have negative value), and our first 
task is to calculate the sum of the pots with plants after the 20th
generation.

Our second task is to calculate the sum of the pots with plants after the
50 * 10 ** 10th generation. Yes, that's 50 Billion.

A snapshot of my eureka moment:
https://hastebin.com/kedobiqutu
"""

from collections import Counter

import re

def sum_plants(pots, offset):
    answer = 0
    for i in range(len(pots)):
        if pots[i] == '#':
            answer += i - offset
    return answer


def generation(pots, rules):
    pots = "...." + pots + "...."
    next_gen = ""
    for i in range(2, len(pots) - 2):
        next_gen += rules[pots[i - 2 : i + 3]]
    if '#' in next_gen[-3]:
        next_gen += '.'
    return next_gen[2:-2]

def main():
    with open("input/day12input_a2") as f:
        raw_data = f.read().splitlines()

    m = re.search("([#.]+)", raw_data[0])

    pots = m.group(1)
    rules = {}
    for l in raw_data[2:]:
        pattern, result = re.search("([#.]{5}).*([#.])", l).groups()

        rules[pattern] = result

    offset = 5
    pots = 5 * '.' + pots
    last_score = 0
    last_diff = 3 * [0]
    print(f"{0:4}({0:5},{0:4}) {pots}")
    for i in range(1, 50 * 10 ** 10):
        pots = generation(pots, rules)
        score = sum_plants(pots, offset)
        if i == 20:
            score_20 = score
        diff = score - last_score
        pre = f"{i:4}({score:5},{diff:4}) "
        print(f"{pre}{pots[:130]}")
        last_score = score
        last_diff.append(diff)
        if len(set(last_diff[-3:])) == 1:
            break

    score_50e10 = (5 * 10 ** 10 - i) * diff + score
    print(f"Part 1  (20th gen):  {score_20}")
    print(f"Part 2 (50Bth gen):  {score_50e10}")

if __name__ == '__main__':
    main()
