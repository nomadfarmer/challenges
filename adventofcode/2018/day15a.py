#!/usr/bin/env python3
"""
Advent of Code 2018 - Day 15 - Beverage Bandits
https://adventofcode.com/2018/day/15

Roguelike!

Backup copy of day15.py so I can safely copy code that changed back into this file.
"""

from termcolor import colored
from copy import deepcopy
from collections import deque
import sys

class Unit():
    def __init__(self, location, power=3):
        self.hp = 200
        self.power = power
        self.location = location

    def move(self, enemies, obstacles):
        if locs(enemies) & adjacent(self.location):
            return  # Don't need to move, we can already attack
        if not enemies:
            print(f'{self.location}: Nothing to move towards. {turn}')
            total_hp = sum([x.hp for x in (elves | goblins)])
            print('Turn', turn, 'total_hp:', total_hp, 'product:',
                  colored(turn * total_hp, 'red'))

            return

        # targets variable name sucks. It winds up being a dict with the
        # first step of a potential path as the key and the number of
        # steps to attacking range as the value.
        targets = set()

        for e in enemies:
            for t in adjacent(e.location) - obstacles:
                targets.add(t)

        if targets:
            self.location = next_step_on_path(self.location, targets,
                                              obstacles)

    def attack(self, enemies):
        e_hp = {}
        ad = adjacent(self.location)
        for e in enemies:
            if e.location in ad:
                e_hp[e] = e.hp
        if e_hp:
            min_hp = min(e_hp.values())
            e_hp = [x for x in e_hp.keys() if e_hp[x] == min_hp]
            victim = sorted(e_hp, key=reading_order)[0]
            # print(f'{self.location} Attacking {victim.location}')
            victim.rec_damage(self.power, enemies)

    def rec_damage(self, damage, friends):
        self.hp -= damage
        # print(f'            {-damage} ({self.hp})')
        if self.hp <= 0:
            friends.remove(self)

    def __str__(self):
        return colored(str(self.hp), 'blue' if self in elves else 'red')


def locs(*args):
    obstacles = set()
    for i in args:
        for j in i:
            if type(j) is tuple:
                obstacles.add(j)
            else:
                obstacles.add(j.location)
    return obstacles


def adjacent(t):
    options = set()
    for i in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        options.add((t[0] + i[0], t[1] + i[1]))
    return options


def next_step_on_path(start, dest, obs):
    """ start point (x, y) tuple
    destination: (x, y) tuple or set of (x, y) tuples
    obstacles: set of (x, y) tuples
    returns (x, y) tuple of best first step (or start if no steps
    are possible
    """

    dest = set(dest)  # Turn single tuple into set
    path = {}
    for d in dest:
        path[d] = [0, {d}]
    frontier = deque(path.keys())
    # while start not in path.keys() and growing:
    while frontier and start not in path:
        i = frontier.popleft()
        steps = path[i][0] + 1
        for j in adjacent(i) - obs:
            if j not in path or path[j][0] > steps:
                path[j] = [steps, path[i][1]]
                frontier.append(j)
            elif path[j][0] == steps and path[j][1] not in path[j]:
                path[j][1] = path[j][1] | path[i][1]
                frontier.append(j)

    cands = {}  # Candidate steps
    for i in adjacent(start):
        if i in path:
            cands[i] = path[i]
    if cands:
        shortest = min([cands[i][0] for i in cands.keys()])
        for d in list(cands.keys()):
            if cands[d][0] > shortest:
                cands.pop(d)
        targets = set()
        for d in cands.values():
            for t in d[1]:
                targets.add(t)

        target = sorted(targets, key=reading_order)[0]
        first_steps = [d for d in cands.keys() if target in cands[d][1]]
        return sorted(first_steps, key=reading_order)[0]
    else:
        # no path to dest
        return start


def reading_order(o):
    """ Recieves any object with a location property
    or just a tuple returns y * 1000 + x
    """
    coord = o if type(o) == tuple else o.location
    return (coord[1] * 10**4) + coord[0]


def show_cave():
    print_cave = deepcopy(cave)
    for g in goblins:
        print_cave[g.location[1]][g.location[0]] = colored('G', 'red')
    for e in elves:
        print_cave[e.location[1]][e.location[0]] = colored('E', 'blue')
    for y in range(len(print_cave)):
        u = sorted([x for x in goblins | elves if x.location[1] == y], key=reading_order)
        u = [str(x) for x in u]
        print(''.join(print_cave[y]), ', '.join(u))


# #### Main #####

fn = sys.argv[1] if len(sys.argv) > 1 else "input/day15"
with open(fn) as f:
    raw_data = f.read().splitlines()

goblins = set()
elves = set()
walls = set()

cave = []
for y in range(len(raw_data)):
    cave.append([])
    for x in range(len(raw_data[y])):
        if raw_data[y][x] == 'G':
            g = Unit((x, y))
            goblins.add(g)
            cave[y].append('.')
        elif raw_data[y][x] == 'E':
            e = Unit((x, y))
            elves.add(e)
            cave[y].append('.')
        elif raw_data[y][x] == '#':
            walls.add((x, y))
            cave[y].append('#')
        else:
            cave[y].append(raw_data[y][x])

show_cave()
turn = 0
while elves and goblins:
    for u in sorted(elves | goblins, key=reading_order):
        if u in goblins:
            u.move(elves, locs(elves, goblins, walls))
            u.attack(elves)
        elif u in elves:
            u.move(goblins, locs(elves, goblins, walls))
            u.attack(goblins)
    turn += 1
    show_cave()
    print('Turn', turn)
    # for u in sorted(elves | goblins, key=reading_order):
    #     print(
    #         colored(f'{u.location}: {u.hp}',
    #                 'red' if u in goblins else 'blue'))
    # input()
