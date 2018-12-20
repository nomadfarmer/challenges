#!/usr/bin/env python3
"""
Advent of Code 2018 - Day  - 1
https://adventofcode.com/2018/day/1

More roguelike
"""

import sys
from itertools import permutations
import re

# import collections

# import numpy as np
# from tqdm import tqdm


class Path():
    route = ''
    branches = set()
    after = ''

    def __init__(self, paths):
        self.branches = set()
        child_paths = []
        first_fork = paths.find('(')
        remainder = ''
        if first_fork == -1:
            self.route = paths
        else:
            self.route = paths[0:first_fork]
            forks = 1
            child_start = first_fork + 1
            for i in range(child_start, len(paths)):
                if paths[i] == '(':
                    forks += 1
                elif paths[i] == ')':
                    forks -= 1
                    if forks == 0:
                        # if paths[i - 1] == '|':
                        child_paths.append(paths[child_start:i])
                        child_start = i + 1
                        break
                elif paths[i] == '|' and forks == 1:
                    child_paths.append(paths[child_start:i])
                    child_start = i + 1
            if forks != 0:
                raise IndexError('Fork still open?')

            remainder = paths[i + 1:]
        print('=' * 10, paths, '=' * 10)
        print('My route:', self.route)
        print('Children:', child_paths)
        print('Remainder:', remainder)
        for child in child_paths:
            self.branches.add(Path(child))
        if remainder:
            self.after = Path(remainder)

    def shortest_most_doors(self):
        ''' If there's nothing after you, return your length
        If there is something after you, you want the longer of
        a) your longest branch
        b) your shortest branch plus what comes after
        '''
        cancellations = [''.join(t) for t in permutations('NESW', 4)]
        cancellations = '(' + '|'.join(cancellations) + ')'

        shortest_branch = 0
        longest_branch = 0
        after_length = 0
        branch_lengths = [b.shortest_most_doors() for b in self.branches]

        if branch_lengths:
            shortest_branch = min(branch_lengths)
            longest_branch = max(branch_lengths)

        if self.after:
            after_length = self.after.shortest_most_doors()

        longest_after = max([longest_branch, shortest_branch + after_length])
        own_length = len(re.sub(cancellations, '', self.route))
        return own_length + longest_after

    # def __repr__(self):
    #     lb = 0
    #     rep = ''
    #     rep += (15 * '=') + '\n'
    #     rep += ('My route: ' + self.route) + '\n'
    #     rep += ('My branches: ' + '|'.join([b.route
    #                                         for b in self.branches])) + '\n'
    #     if self.branches:
    #         lb = max([len(b.route) for b in self.branches])

    #     if self.after:
    #         rep += self.after.__repr__()
    #     return rep


fn = sys.argv[1] if len(sys.argv) > 1 else "input/day20"
with open(fn) as f:
    raw_data = f.read().strip().strip('$^')
dir_1 = 'WNE'
dir_2 = 'ENWWW(NEEE|SSE(EE|N))'
dir_3 = '^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$'.strip('$^')
dir_4 = 'ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))'
dir_5 = 'WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))'

path = Path(raw_data)
print(path.shortest_most_doors())
