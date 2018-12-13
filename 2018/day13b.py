#!/usr/bin/env python3
"""
Advent of Code 2018 - Day 13 -
https://adventofcode.com/2018/day/13

"""

import sys
from copy import deepcopy
# from termcolor import colored

NORTH = 0
WEST = 1
SOUTH = 2
EAST = 3
DIR_SYMS = ["^", "<", "v", ">"]
DIRS = [(0, -1), (-1, 0), (0, 1), (1, 0)]

#Relative directions, not E/W
RIGHT = -1
LEFT = 1



class cart:
    direction = 1 # index from DIR_SYMS
    location = (0, 0)
    next_turn = 1
    track = "|"
    collision = False

    def __init__(self, direction, location):
        self.direction = direction
        self.location = location
        self.next_turn = LEFT
        if direction in (0, 2):
            self.track = "|"
        else:
            self.track = "-"


    def move(self, course, carts):
        # print(f"Pre: {self.location}, {self.track}, {DIR_SYMS[self.direction]} {self.next_turn}")
        if self.track ==  "/":
             if self.direction in (NORTH, SOUTH):
                self.turn(RIGHT)
             else:
                self.turn(LEFT)
                # print(self.direction)
        elif self.track == "\\":
            if self.direction in (NORTH, SOUTH):
                self.turn(LEFT)
            else:
                self.turn(RIGHT)
        elif self.track == "+":
            self.turn(self.next_turn)
            self.next_turn -= 1
            if self.next_turn < -1:
                self.next_turn = 1
        new_location = (self.location[0] + DIRS[self.direction][0], self.location[1] + DIRS[self.direction][1])
        self.track = course[new_location[1]][new_location[0]]


        for c in carts:
            if c.location == new_location:
                # for i in range(5):
                #     print(colored(100 * "#", "red"))
                print("Collision at ", new_location)
                self.collision = True
                c.collision = True
                self.location = (-1, -1)
                c.location = (-1, -1)
                carts.remove(c)
                carts.remove(self)
                print("Carts left: ", len(carts))
        # print(f"Post: {new_location}, {self.track}, {DIR_SYMS[self.direction]} {self.collision}")
        if not self.collision:
            self.location = new_location



    def turn(self, lr):
        """lr == +1 for left, -1 for right. We'll assume no larger inputs"""
        self.direction += lr
        self.direction %= 4 # (turn 4 into 0, -1 into 3)

def cart_locs(course, carts):
    cl = []
    for y in range(len(course)):
        cl.append([])
        for x in range(len(course[y])):
            cl[y].append(None)
    for c in carts:
        cl[c.location[1]][c.location[0]] = c
        
    return cl

def main():
    fn = sys.argv[1] if len(sys.argv) > 1 else "input/day13"
    with open(fn) as f:
        course = f.read().splitlines()

    carts = []
    for y in range(len(course)):
        course[y] = list(course[y])
        for x in range(len(course[y])):
            if course[y][x] in DIR_SYMS:
                carts.append(cart(DIR_SYMS.index(course[y][x]), (x, y)))
                course[y][x] = carts[-1].track
    for x in course:
        print(''.join(x))


    done = False
    turns = 0
    while len(carts) > 1:
        turns += 1
        cl = cart_locs(course, carts)
        if len(carts) == 1:
            done = True
        # ghost_course = deepcopy(course)
        for row in cl:
            for c in filter(lambda x: x is not None, row):
                c.move(course, carts)
                collision = c.collision
                # ghost_course[c.location[1]][c.location[0]] = colored(DIR_SYMS[c.direction], "red")

        # if turns > 314:
        #     for row in ghost_course:
        #         print(''.join(row))
        #     print (turns)
        #     input()
    print(c.location, turns)



if __name__ == '__main__':
    main()
