#!/usr/bin/env python3
"""
Advent of Code 2018 - Day 20 - A Regular Map
https://adventofcode.com/2018/day/20

Starting with a string that represents directions, calculate the shortest
distance to the room which requires the most steps to get to.
"""

import sys


class Path():
    route = ''
    branches = set()
    after = ''

    def __init__(self, paths, rooms, starts):
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
            remainder = paths[i + 1:]
        pre_child_ends = set()
        for s in starts:
            loc = s
            path_to_here = rooms[loc]
            dirs = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
            for d in self.route:
                loc = (loc[0] + dirs[d][0], loc[1] + dirs[d][1])
                path_to_here += d
                if loc not in rooms or len(rooms[loc]) > len(path_to_here):
                    rooms[loc] = path_to_here
            pre_child_ends.add(loc)

        self.ends = set()
        for child in child_paths:
            b = Path(child, rooms, pre_child_ends)
            self.branches.add(b)
            self.ends |= b.ends

        if not child_paths:
            self.ends = pre_child_ends

        if remainder:
            self.after = Path(remainder, rooms, self.ends)

        # print('=' * 10, paths, '=' * 10)
        # print('My route:', self.route)
        # print('Children:', child_paths)
        # print('Remainder:', remainder)


fn = sys.argv[1] if len(sys.argv) > 1 else "input/day20"
with open(fn) as f:
    raw_data = f.read().strip().strip('$^')
dir_1 = 'WNE'
dir_2 = 'ENWWW(NEEE|SSE(EE|N))'
dir_3 = '^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$'.strip('$^')
dir_4 = 'ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))'
dir_5 = 'WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))'

start = {(0, 0)}
rooms = {(0, 0): ''}

path = Path(raw_data, rooms, start)

print('Part 1:', max([len(x) for x in rooms.values()]))
print('Part 2:', len([x for x in rooms.values() if len(x) >= 1000]))
print('Total rooms:', len(rooms))
