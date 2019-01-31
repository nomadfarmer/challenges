#!/usr/bin/env python3
"""
Turn ascii art into vectors in the format of the puzzle at
https://adventofcode.com/2018/day/10
"""
import sys
import random

random.seed()
origin_x = random.randrange(1000)
origin_y = random.randrange(1000)
time = random.randrange(5000, 30000)

with open(sys.argv[1]) as f:
    message = f.read().splitlines()

velocities = list(range(-5, 0)) + list(range(1, 6))

print(f"Time of message: {time}. Origin: {origin_x},{origin_y}")
for y in range(len(message)):
    for x in range(len(message[y])):
        if message[y][x] != ' ':
            vx = random.choice(velocities)
            vy = random.choice(velocities)
            px = x + (vx * -time)
            py = y + (vy * -time)
            symbol = message[y][x]
            print("position=<{: d}, {: d}> velocity=<{: d}, {: d}> symbol={}".format(
                px, py, vx, vy, symbol))
