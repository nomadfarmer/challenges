#!/usr/bin/env python3
"""
Codewars 6k puzzle - Pascal's Triangle
https://www.codewars.com/kata/5226eb40316b56c8d500030f/train/python

Return a (1d) list of the values of pascal's triangle up to n rows.
Each row in the triangle has a length one longer than the previous
row. Each entry in each row has a sum of the two entries above it, as
demonstrated here:
          1
        1   1
      1   2   1
    1   3   3   1
  1   4   6   4   1
1   5  10  10   5   1
"""


def pascals_triangle(n):
    triangle = [1]
    row_length = 1
    for i in range(2, n + 1):
        row_length += 1
        row = [] * i
        row[0] = row[-1] = 1
        for j in range(1, row_length - 1):
            row[j] = triangle[


def test_pt_1_to_4():
    assert pascals_triangle(1) == [1]
    assert pascals_triangle(2) == [1, 1, 1]
    assert pascals_triangle(3) == [1, 1, 1, 1, 2, 1]
    assert pascals_triangle(4) == [1, 1, 1, 1, 2, 1, 1, 3, 3, 1]
