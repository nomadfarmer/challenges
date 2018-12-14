# /usr/bin/env python3
"""
Advent of Code 2017 - Day 07 - Recursive Circus
https://adventofcode.com/2017/day/7

Part 1
We're given nodes of a tree in random order. Each node has a name, weight,
and the names of any children it has. Our job is to find the name of the
root node.

Although I imagine part 2 will require building a tree (and that weights
will become relevant), I'm going to hack part 1 by creating a set of all
nodes and a set of all nodes that are children and finding the difference.
"""

import re

with open("ms07input") as f:
    raw_data = f.read().splitlines()

print(raw_data)

nodes = set()
children = set()

for l in raw_data:
    names = re.findall(r'([a-z]+)', l)
    nodes.add(names[0])
    if len(names) > 1:
        for c in names[1:]:
            children.add(c)
print(nodes ^ children)
