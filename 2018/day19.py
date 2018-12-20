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
print('IP: reg', ip_reg)

instructions = []

for i in range(1, len(raw_lines)):
    line = raw_lines[i].split(' ')
    op = op_names.index(line[0])
    regs = tuple([int(line[x]) for x in range(1, 4)])
    instructions.append((op, ) + regs)


def cpu(code, ip_reg, start_reg, time=0):
    i = 0
    reg = start_reg[:]
    ip = 0
    while reg[ip_reg] >= 0 and reg[ip_reg] < len(code) \
          and (time == 0 or i <= time):
        reg[ip_reg] = ip
        op = instructions[ip]
        reg = operations[op[0]](reg, op)
        ip = reg[ip_reg]
        ip += 1
        i += 1
    return reg

def sum_of_divisors(n):
    s = 0
    for i in range(1, int(n**.5) + 1):
        if n % i == 0:
            s += i + (n // i)
    return s


n = max(cpu(instructions, ip_reg, [0, 0, 0, 0, 0, 0], 20))
part1 = sum_of_divisors(n)
n = max(cpu(instructions, ip_reg, [1, 0, 0, 0, 0, 0], 20))
part2 = sum_of_divisors(n)

print('Part 1:', part1)
print('Part 2:', part2)
