#!/usr/bin/env python3
"""
Advent of Code 2018 - Day 15 - Beverage Bandits
https://adventofcode.com/2018/day/15

Roguelike!
"""

from termcolor import colored
from copy import deepcopy
import sys


class Unit():
    def __init__(self, location):
        self.hp = 200
        self.power = 3
        self.location = location

    def move(self, enemies, obstacles):
        if locs(enemies) & adjacent(self.location):
            return  # Don't need to move, we can already attack
        if not enemies:
            print(f'{self.location}: Nothing to move on. {turn}')
            total_hp = sum([x.hp for x in (elves | goblins)])
            print('Turn', turn, 'total_hp:', total_hp, 'product:',
                  colored(turn * total_hp, 'red'))

            return

        # targets variable name sucks. It winds up being a dict with the
        # first step of a potential path as the key and the number of
        # steps to attacking range as the value.
        targets = {}
        en_dist = {}

        # Find the manhattan distance to each enemy. Only try to path
        # to the closest 25%ish of enemies.
        for e in enemies:
            d = abs(self.location[0] - e.location[0]) \
                + abs(self.location[1] - e.location[1])
            en_dist[e] = d
        # max_dist = sorted(en_dist.values())[
        #   2 if len(en_dist) > 2 else len(en_dist) - 1]
        dists = sorted(en_dist.values())
        max_dist = dists[((len(dists) // 5) + 1) if len(dists) >= 5 else -1]
        # for e in enemies:
        for e in [x for x in en_dist.keys() if en_dist[x] <= max_dist]:
            for t in adjacent(e.location) - obstacles:
                path = next_step_on_path(self.location, t, obstacles)
                if path:
                    if path[0] not in targets or targets[path[0]] > path[1]:
                        targets[path[0]] = path[1]
        if targets:
            shortest = min(targets.values())
            targets = [x for x in targets.keys() if targets[x] == shortest]
            # old_location = self.location
            self.location = sorted(targets, key=reading_order)[0]
            # print(f'{old_location}->{self.location}')
        # else:
        #     print(f'{self.location}: No path')

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
    """ start point and destination: (x, y) tuple
        obstacles: set of (x, y) tuples
    """

    path = {dest: 0}  # {coordinate: number of steps from destination}
    growing = True
    while start not in path.keys() and growing:
        path_keys = list(path.keys())[:]
        for i in path_keys:
            steps = path[i] + 1
            for j in adjacent(i) - obs:
                # print(path, j)
                if j not in path or path[j] > steps:
                    path[j] = steps
        if len(path) <= len(path_keys):
            growing = False
    cands = {}  # Candidates
    for i in adjacent(start):
        if i in path:
            cands[i] = path[i]
    if cands:
        shortest = min(cands.values())
        cands = [x for x in cands.keys() if cands[x] == shortest]
        return (sorted(cands, key=reading_order)[0], shortest)
    else:
        # no path to dest
        return None


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
    for y in print_cave:
        print(''.join(y))


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
