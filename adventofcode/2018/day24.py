#!/usr/bin/env python3
"""
Advent of Code 2018 - Day 24 - Immune System Simulator 20XX
https://adventofcode.com/2018/day/24

"""

import sys
import re

fn = sys.argv[1] if len(sys.argv) > 1 else "input/day24"
verbose = True
part1 = False


class Group:
    name = ""
    units = 0
    hp_per_unit = 0
    immunities = []
    weaknesses = []
    damage_type = ''
    damage = 0
    initiative = 0
    targetted = False

    def __init__(self, input_string, team_name, team):
        self.name = "{} {}".format(team_name, len(team) + 1)
        self.team = team
        m = re.search(r'(?:immune to (.*?)[;)])', input_string)
        if m:
            self.immunities = m.group(1).split(', ')
        else:
            self.immunities = []

        m = re.search(r'(?:weak to (.*?)[;)])', input_string)
        if m:
            self.weaknesses = m.group(1).split(', ')
        else:
            self.weaknesses = []

        m = re.search(r'(\w+) damage', input_string)
        self.damage_type = m.group(1)

        self.units, self.hp_per_unit, self.damage, self.initiative = [
            int(i) for i in re.findall(r'(\d+)', input_string)
        ]
        self.targetted = False
        self.target = False

    def power(self):
        return self.damage * self.units

    def targetted_by(self, enemy):
        if enemy:
            self.targetted = True
        else:
            self.targetted = False

    def select_target(self, enemies):
        def target_o(g):
            bonus = 1
            if self.damage_type in g.weaknesses:
                bonus = 2
            elif self.damage_type in g.immunities:
                bonus = 0
            damage = self.damage * self.units * bonus
            return (damage, g.power(), g.initiative)

        pot_targets = [
            e for e in enemies
            if not e.targetted and self.damage_type not in e.immunities
        ]
        if pot_targets:
            t = max(pot_targets, key=target_o)
            t.targetted_by(self)
            self.target = t

    def attack(self):
        if self not in self.team:
            return False
        if self.target:
            if verbose:
                print(self.name + ' attacks', self.target.name + ' ', end='')
            self.target.hit(self.units * self.damage, self.damage_type)
        self.target = False

    def hit(self, hp, damage_type):
        bonus = 2 if damage_type in self.weaknesses else 1
        bonus = 0 if damage_type in self.immunities else bonus
        dead_units = (hp * bonus) // self.hp_per_unit
        self.units -= dead_units
        if verbose:
            print('killing {} units ({} remain)'.format(
                dead_units, self.units))
        if self.units <= 0:
            self.team.remove(self)
        self.targetted = False
        if self.target:
            self.target.targetted_by(None)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        s = self.name + ': '
        s += str(self.units) + ' units with '
        s += str(self.hp_per_unit) + ' hp each '
        if self.immunities or self.weaknesses:
            s += '('
            if self.immunities:
                s += 'immune to ' + ', '.join(self.immunities)
                s += '; ' if self.weaknesses else ''
            if self.weaknesses:
                s += 'weak to ' + ', '.join(self.weaknesses)
            s += ') '
        s += 'attack of ' + str(self.damage) + ' ' + self.damage_type
        s += ' with initiative ' + str(self.initiative)
        return s


def select_o(g):
    return (g.power(), g.initiative)


def attack_o(g):
    return (g.initiative)


with open(fn) as f:
    raw_data = f.read().splitlines()


# Starting from 0, we entered an infinite loop for boosts 49-51
# I changed it manually to 50 and 51. Later I'lll investigate how
# to detect the infinite loop and break through.
if not part1:
    boost = 52


reindeer_won = False
while not reindeer_won:
    immune_system = set()
    infection = set()
    for l in raw_data:
        if l.startswith('Immune'):
            current_army = immune_system
        elif l.startswith('Infection'):
            current_army = infection
        elif l.strip():
            if current_army is immune_system:
                army_name = 'Immune'
            else:
                army_name = 'Infection'
            current_army.add(Group(l, army_name, current_army))
    for g in immune_system:
        g.damage += boost
    if verbose:
        print("Immune system groups:")
        for g in immune_system:
            print(g)
        print("Infection groups:")
        for g in infection:
            print(g)
        print('=' * 80)
    
    while immune_system and infection:
        select = sorted(immune_system | infection, key=select_o, reverse=True)
        for g in select:
            g.select_target(immune_system if g in infection else infection)
        attack = sorted(immune_system | infection, key=attack_o, reverse=True)
        for g in attack:
            g.attack()
        if verbose:
            # input()
            print('=')

    print('Winner:', 'reindeer!' if immune_system else 'infection...')
    survivors = sum([g.units for g in immune_system | infection])
    print('Remaining units: ', survivors)
    if part1:
        break
    if not immune_system:
        boost += 1
        print('Trying boost', boost)
    else:
        reindeer_won = True
