#!/usr/bin/env python3
"""Advent of Code 2017 - Day 04 - High-Entropy Passphrases
https://adventofcode.com/2017/day/4

Read a file and count the number of lines which have no duplicate words.

"""
import itertools


def count_valid_passphrases(filename):
    with open(filename) as f:
        passphrases = f.read().strip().splitlines()

    valid_phrases = 0
    for p in passphrases:
        words = p.split(" ")
        valid = True
        for w in words:
            if words.count(w) > 1:
                valid = False
                break
        if valid:
            valid_phrases += 1
    return valid_phrases


def count_valid_passphrases_2(filename):
    with open(filename) as f:
        passphrases = f.read().strip().splitlines()
    valid_phrases = 0
    for p in passphrases:
        valid = True
        for w1, w2 in itertools.combinations(p.split(" "), 2):
            if sorted(w1) == sorted(w2):
                valid = False
                break
        if valid:
            valid_phrases += 1
    return valid_phrases


# assert count_valid_passphrases("ms04input_test") == 2
# print(count_valid_passphrases("ms04input"))

assert count_valid_passphrases_2("ms04input_test2") == 3
print(count_valid_passphrases_2("ms04input"))
