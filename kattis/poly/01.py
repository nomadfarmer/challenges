#!/usr/bin/env python3
import sys

def naive_powers_and_mod(a, b):
    return sum([x ** b for x in range(1, a + 1)]) % a

# print(form(2, 3))
# print(form(3, 7))
# print(form(12345678, 9))


def polygon_area(vertices):
    polys = []

    poly_count = 0
    for i in range(len(vertices)):
        line = [int(n) for n in vertices[i].split(' ')]
        if len(line) == 1 and line[0] != 0:
            poly_count += 1
            polys.append([])
        elif len(line) > 1:
            polys[poly_count - 1].append(tuple(line))

    for p in polys:
        a = 0
        for i in range(len(p)):
            a -= p[i][0] * p[(i + 1) % len(p)][1]
            a += p[i][1] * p[(i + 1) % len(p)][0]
        direction = 'CW' if a > 0 else 'CCW'
        print("{} {}".format(direction, abs(a / 2)))


polygon_area(sys.stdin.readlines())
