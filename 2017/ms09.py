#!/usr/bin/env python3
"""
Advent of Code 2017 - Day  - Stream Processing
https://adventofcode.com/2017/day/9

"""

from tqdm import tqdm
# import numpy as np
# import re
# import collections
# import sys


def test_stream_group_count():
    assert process_stream("{}")[0] == 1
    assert process_stream("{{{}}}")[0] == 3
    assert process_stream("{{},{}}")[0] == 3
    assert process_stream("{{{},{},{{}}}}")[0] == 6
    assert process_stream("{<{},{},{{}}>}")[0] == 1
    assert process_stream("{<a>,<a>,<a>,<a>}")[0] == 1
    assert process_stream("{{<a>},{<a>},{<a>},{<a>}}")[0] == 5
    assert process_stream("{{<!>},{<!>},{<!>},{<a>}}")[0] == 2


def test_stream_score():
    assert process_stream("{}")[1] == 1
    assert process_stream("{{{}}}")[1] == 6
    assert process_stream("{{},{}}")[1] == 5
    assert process_stream("{{{},{},{{}}}}")[1] == 16
    assert process_stream("{<a>,<a>,<a>,<a>}")[1] == 1
    assert process_stream("{{<ab>},{<ab>},{<ab>},{<ab>}}")[1] == 9
    assert process_stream("{{<!!>},{<!!>},{<!!>},{<!!>}}")[1] == 9
    assert process_stream("{{<a!>},{<a!>},{<a!>},{<ab>}}")[1] == 3


def process_stream(stream: str):
    groups = 0
    open_groups = 0
    score = 0
    escaped = False
    in_garbage = False
    for c in tqdm(stream):
        if escaped:
            escaped = False
        elif c == '!':
            escaped = True
        elif c == '<':
            in_garbage = True
        elif in_garbage:
            if c == '>':
                in_garbage = False
        elif c == '{':
            groups += 1
            open_groups += 1
            score += open_groups
        elif c == '}':
            open_groups -= 1
            if open_groups < 0:
                raise ValueError('Invalid input: Closed more groups than opened')
    print(groups)
    return (groups, score)


def main():
    with open("input/ms09") as f:
        stream = f.read().strip()

    test_stream_group_count()
    test_stream_score()
    print(process_stream(stream))


# Commented to run in elpy
# if __name__ == '__main__':
main()
