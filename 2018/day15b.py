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
    growing = True
    # while start not in path.keys() and growing:
    while growing:
        path_keys = list(path.keys())[:]
        for i in path_keys:
            steps = path[i][0] + 1
            for j in adjacent(i) - obs:
                # print(path, j)
                if j not in path or path[j][0] > steps:
                    path[j] = [steps, path[i][1]]
                elif path[j][0] == steps:
                    path[j][1] = path[j][1] | path[i][1]

        if len(path) <= len(path_keys):
            growing = False
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

gob_starts = set()
elf_starts = set()
walls = set()

goblins = set()
elves = set()

cave = []
for y in range(len(raw_data)):
    cave.append([])
    for x in range(len(raw_data[y])):
        if raw_data[y][x] == 'G':
            gob_starts.add((x, y))
            cave[y].append(colored('.', 'white'))
        elif raw_data[y][x] == 'E':
            elf_starts.add((x, y))
            cave[y].append(colored('.', 'white'))
        elif raw_data[y][x] == '#':
            walls.add((x, y))
            cave[y].append('#')
        else:
            cave[y].append(colored(raw_data[y][x], 'white'))

# show_cave()
elf_power = 3  # Previous run suggests we can start looking here
done = False
turn_start = 0
while not done:
    elf_power += 1
    goblins = set()
    elves = set()
    turn = turn_start
    print(colored('=' * 30, 'red'))
    print(colored('Trying elf attack of', 'red'), colored(elf_power, 'blue'))
    print(colored('=' * 30, 'red'))
    for e in elf_starts:
        elves.add(Unit(e, elf_power))
    for g in gob_starts:
        goblins.add(Unit(g))
    elf_count = len(elves)
    while len(elves) == elf_count and goblins:
        for u in sorted(elves | goblins, key=reading_order):
            if u in goblins:
                u.move(elves, locs(elves, goblins, walls))
                u.attack(elves)
            elif u in elves:
                u.move(goblins, locs(elves, goblins, walls))
                u.attack(goblins)
        turn += 1
        # show_cave()
        # print('Turn', turn)
    if len(elves) < elf_count:
        show_cave()
        print(f'Elf down after turn {turn}')
        print(
            colored('Leave no elf behind! We need more power!\n',
                    'magenta'))
    else:
        done = True
        show_cave()
        print(f'Flawless victory! Power level {elf_power}')
        total_hp = sum([x.hp for x in (elves | goblins)])
        print('Turn', turn, 'total_hp:', total_hp, 'product:',
              colored(turn * total_hp, 'red'))

        # for u in sorted(elves | goblins, key=reading_order):
        #     print(
        #         colored(f'{u.location}: {u.hp}',
        #                 'red' if u in goblins else 'blue'))
        # input()
