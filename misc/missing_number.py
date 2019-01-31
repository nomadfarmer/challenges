#!/usr/bin/env python3
""" Puzzle from a friend's tech interview.
An unordered list contains all ints from 1 to n (inclusive),
except one. Find the missing int.

Write a bad implementation, then the best you can think of.
""" 


def bad_f(l, n):
    candidates = []
    for i in range(n):
        candidates.append(i + 1)
    # (already O(n)
    for i in len(candidates):
        try:
            l.remove(candidates[i])
        except:
            return (candidates[i])


def o_2n_f(l, n):
    s = set(range(1, n + 1))
    for i in l:
        s.remove(i)
    return s.pop()


def o_n_f(l, n):
    return ((n * (n + 1)) / 2) - sum(l)
