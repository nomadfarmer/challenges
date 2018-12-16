#!/usr/bin/env python3
"""
Advent of Code 2018 - Day 16 - Chronal Classification
https://adventofcode.com/2018/day/16

assembler interpreter?

"""

import re
import sys
import os

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

fn = sys.argv[1] if len(sys.argv) > 1 else "input/day16"
with open(fn) as f:
    raw_data = f.read().splitlines()

ops = []
for i in range(0, 796):
    raw_data.pop()  # Blank line
    post = re.findall(r'(\d+)', raw_data.pop())
    post = tuple([int(x) for x in post])

    op = re.findall(r'(\d+)', raw_data.pop())
    op = tuple([int(x) for x in op])

    pre = re.findall(r'(\d+)', raw_data.pop())
    pre = tuple([int(x) for x in pre])

    ops.append((pre, op, post))

ambiguity = {}
opcode_options = {}
for i in range(16):
    opcode_options[i] = set()
for pre, op, post in ops:
    matches = []
    for o in operations:
        try:
            match = tuple(o(pre, op)) == post
        except IndexError:
            match = False
        matches.append(match)
    match_count = matches.count(True)

    opcode_options[op[0]] |= set(
        op_names[i] for i in range(len(op_names)) if matches[i])
    if match_count in ambiguity:
        ambiguity[match_count] += 1
    else:
        ambiguity[match_count] = 1
print('Instruction ambiguity levels (possibilities: count)')
rows, columns = os.popen('stty size', 'r').read().split()
columns = int(columns) if int(columns) <= 95 else 95

scale = (columns - 12) / max(ambiguity.values())
for a in sorted(ambiguity.keys()):

    print(f'{a:3}: {ambiguity[a]:3} ' + '*' * (int(scale * ambiguity[a])))
print('')
three_or_better = sum(ambiguity[x] for x in ambiguity.keys() if x >= 3)
print('Part 1: ', three_or_better,
      'operations had an ambiguity of 3 or greater\n\n')

print('Opcode ambiguity\n' + (int(columns) - 2) * '=')
for a in sorted(opcode_options.keys(), key=lambda x: len(opcode_options[x])):
    names = ', '.join([x for x in sorted(opcode_options[a])])
    if len(names) + 9 > columns:
        for i in range((len(names) + 9) // (columns - 8)):
            nl = names.rfind(',', i * columns,  (i * columns) + columns - 8)
            names = names[:nl + 1] + '\n' + 8 * ' ' + names[nl + 1:]
            
    print(f'{a:3}:{len(opcode_options[a]): 3} ({names}) ')
print((int(columns) - 2) * '=' + '\n')

op_map = {}
while opcode_options:
    for op in range(16):
        if op in opcode_options and len(opcode_options[op]) == 1:
            op_name = opcode_options[op].pop()
            op_map[op] = op_names.index(op_name)
            for v in opcode_options.values():
                v -= {op_name}
            opcode_options.pop(op)
            break
print()
c = 4 if columns > 42 else 2
top = '-' * ((10 * c) + 1)
print('opcode values:')
print(top)
for i in range(16 // c):
    l = '|'
    for o in range(i, i + (16 - 16 // c) + 1, 16 // c):
        l += f'{o:2}: {op_names[op_map[o]]} |'
    print(l)
print(top)

with open('input/day16b') as f:
    prog = f.readlines()

reg = [0, 0, 0, 0]
for i in range(len(prog)):
    op = [int(x) for x in prog[i].split(' ')]
    reg = operations[op_map[op[0]]](reg, op)

print(f'After {i} operations, the registers are {reg}')
