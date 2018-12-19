#!/usr/bin/env python3
"""
Advent of Code 2018 - Day 19 -
https://adventofcode.com/2018/day/19

"""


import sys
# import re
# import collections

# import numpy as np
# from tqdm import tqdm


truth_table = {True: 1, False: 0}


def addr(reg, opcode):
    """reg: tuple containing the starting states of the registers
    opcode: tuple containing [opcode, A, B, C]
    reg[C] = reg[A] + reg[B]
    """
    reg = list(reg)
    op, a, b, c = opcode
    reg[c] = reg[a] + reg[b]
    return reg


def addi(reg, opcode):
    reg = list(reg)
    op, a, b, c = opcode
    reg[c] = reg[a] + b
    return reg


def mulr(reg, opcode):
    reg = list(reg)
    op, a, b, c = opcode
    reg[c] = reg[a] * reg[b]
    return reg


def muli(reg, opcode):
    reg = list(reg)
    op, a, b, c = opcode
    reg[c] = reg[a] * b
    return reg


def banr(reg, opcode):
    reg = list(reg)
    op, a, b, c = opcode
    reg[c] = reg[a] & reg[b]
    return reg


def bani(reg, opcode):
    reg = list(reg)
    op, a, b, c = opcode
    reg[c] = reg[a] & b
    return reg


def borr(reg, opcode):
    reg = list(reg)
    op, a, b, c = opcode
    reg[c] = reg[a] | reg[b]
    return reg


def bori(reg, opcode):
    reg = list(reg)
    op, a, b, c = opcode
    reg[c] = reg[a] | b
    return reg


def setr(reg, opcode):
    reg = list(reg)
    op, a, b, c = opcode
    reg[c] = reg[a]
    return reg


def seti(reg, opcode):
    reg = list(reg)
    op, a, b, c = opcode
    reg[c] = a
    return reg


def gtir(reg, opcode):
    reg = list(reg)
    op, a, b, c = opcode
    reg[c] = truth_table[a > reg[b]]
    return reg


def gtri(reg, opcode):
    reg = list(reg)
    op, a, b, c = opcode
    reg[c] = truth_table[reg[a] > b]
    return reg


def gtrr(reg, opcode):
    reg = list(reg)
    op, a, b, c = opcode
    reg[c] = truth_table[reg[a] > reg[b]]
    return reg


def eqir(reg, opcode):
    reg = list(reg)
    op, a, b, c = opcode
    reg[c] = truth_table[a == reg[b]]
    return reg


def eqri(reg, opcode):
    reg = list(reg)
    op, a, b, c = opcode
    reg[c] = truth_table[reg[a] == b]
    return reg


def eqrr(reg, opcode):
    reg = list(reg)
    op, a, b, c = opcode
    reg[c] = truth_table[reg[a] == reg[b]]
    return reg


op_names = [
    'addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr',
    'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr'
]

operations = [
    addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri,
    gtrr, eqir, eqri, eqrr
    ]


fn = sys.argv[1] if len(sys.argv) > 1 else "input/day19"
with open(fn) as f:
    raw_lines = f.read().splitlines()

ip_reg = int(raw_lines[0].split(' ')[1])
print(ip_reg)

instructions = []

for i in range(1, len(raw_lines)):
    line = raw_lines[i].split(' ')
    print(line)
    op = op_names.index(line[0])
    regs = tuple([int(line[x]) for x in range(1, 4)])
    # print(f'op: {op} ({op_names[op]}), registers: {regs}')
    instructions.append((op,) + regs)

# print(instructions)
# exit()
ip = 0
# reg = [1, 0, 0, 0, 0, 0]
"""
[0, 34, 0, 0, 10550400, 10551296]
[1, 7, 1, 10551296, 1, 10551296]
[3, 7, 2, 5275648, 1, 10551296]
[7, 7, 4, 2637824, 1, 10551296]
[14, 7, 7, 1507328, 1, 10551296]
[22, 7, 8, 1318912, 1, 10551296]
[36, 7, 14, 753664, 1, 10551296]
[52, 7, 16, 659456, 1, 10551296]
[75, 7, 23, 458752, 1, 10551296]
[103, 7, 28, 376832, 1, 10551296]
[135, 7, 32, 329728, 1, 10551296]
[181, 7, 46, 229376, 1, 10551296]

"""

reg = [0, 0, 0, 0, 0, 0]

while ip in range(0, len(instructions)):
    reg[ip_reg] = ip
    op = instructions[ip]
    new_reg = operations[op[0]](reg, op)
    if new_reg[0] != reg[0]:
        print(new_reg)
    reg = new_reg
    ip = reg[ip_reg]
    ip += 1
    # print(reg)
print('Final registers:\n', reg)
# print(f'After {i} operations, the registers are {reg}')
