#/usr/bin/env python3
"""
Advent of Code 2017 - Day 08 - I Heard You Like Registers
https://adventofcode.com/2017/day/8

Take a list of instructions in the format
b inc 5 if a > 1
and execute them. Registers are always assumed to start at 0.

After all instructions are complete, what is the largest value in 
any register?

Part 2: What was the largest value any register ever held?
"""

import re

with open("ms08input") as f:
    raw_data = f.read().splitlines()

pattern = re.compile(r"([a-z]+) (inc|dec) (-?\d+) if ([a-z]+) ([<>=!]+) (-?\d+)")
regs = {}
top_value = 0

for l in raw_data:
    m = pattern.match(l)

    reg, instruction, value, comp_reg, comp_op, comp_val = m.groups()
    for r in (reg, comp_reg):
        if r not in regs:
            regs[r] = 0
    
    if eval(f'{regs[comp_reg]} {comp_op} {comp_val}'):
        k = 1 if instruction == 'inc' else -1
        regs[reg] += k * int(value)
        if regs[reg] > top_value:
            top_value = regs[reg]
print("Largest value at completion:", max(regs.values()))
print("Largest value ever:         ", top_value)
        
        
