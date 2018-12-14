#!/usr/bin/env python3
"""Advent of Code 2017 - Day 05 - A Maze of Twisty Trampolines, All Alike
https://adventofcode.com/2017/day/3
"""


def traverse(instructions):
    jumps = 0
    position = 0
    instructions = instructions[:]
    
    while position in range(len(instructions)):
        if instructions[position] < 3:
            offset = 1
        else:
            offset = -1
        instructions[position] += offset
        position += instructions[position] - offset
        jumps += 1

    return jumps

with open("ms05input") as f:
    input_ = f.read().strip().splitlines()

input_ = list(map(int, input_))

print(traverse(input_))
