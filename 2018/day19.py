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
    l = raw_lines[i].split(' ')
    print(l)
    op = op_names.index(l[0])
    regs = tuple([int(l[x]) for x in range(1, 4)])
    # print(f'op: {op} ({op_names[op]}), registers: {regs}')
    instructions.append((op,) + regs)

# print(instructions)
# exit()
ip = 0
reg = [1, 0, 0, 0, 0, 0]
while ip in range(0, len(instructions)):
    reg[ip_reg] = ip
    op = instructions[ip]
    new_reg = operations[op[0]](reg, op)
    print(ip, reg, op_names[op[0]], [op[x] for x in range(1, 4)], new_reg)
    input()
    reg = new_reg
    ip = reg[ip_reg]
    ip += 1
    # print(reg)

print(reg)
# print(f'After {i} operations, the registers are {reg}')
