#!/usr/bin/env python3
"""
Advent of Code 2018 - Day 24 - Immune System Simulator 20XX
https://adventofcode.com/2018/day/24

"""

import sys
import re
# import collections

# import numpy as np
# from tqdm import tqdm


fn = sys.argv[1] if len(sys.argv) > 1 else "input/day24"


class Group:
    units = 0
    immunities = []
    weaknesses = []
    damage_type = ''
    hp_per_unit = 0
    
    pass


with open(fn) as f:
    raw_data = f.read().splitlines()

for l in raw_data:
    pass
