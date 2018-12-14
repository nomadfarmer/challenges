#!/usr/bin/env python3
"""Advent of Code 2017 - Day 03 - Spiral Memory
https://adventofcode.com/2017/day/3

In today's puzzles we'll be dealing with a data structure whose first 
entry is at the center of a matrix and subsequent entries wrap in a 
spiral (First right, then anti-clockwise if it should prove to matter
in the second part of the puzzle)

"""


def ms03_p1(n):
    """Find the (manhattan) distance between the nth cell in the matrix
    and the center.
    """

    if n == 1:
        return 0

    n -= 1

    shell_side = 3
    shells = 1

    while n > (shell_side - 1) * 4:
        n -= (shell_side - 1) * 4
        shells += 1
        shell_side += 2

    return shells + abs((n % (shell_side - 1)) - shell_side // 2)


def ms03_p2(n):
    """ The mathy solution above won't work for part 2. The value in
    each cell is equal to the sum of all the surrounding cells that 
    existed when it was created. What's the first sum that's greater
    than our puzzle input (325489)
    """
    pass


class Spiral:
    cells = {}
    last_cell = None
    heading = 0
    dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
    max_ = [0, 0, 0, 0]

    def add_cell(self):
        if not self.last_cell:
            self.last_cell = (0, 0)
            self.cells[self.last_cell] = new_value = 1
        else:
            new_cell = (self.last_cell[0] + self.dirs[self.heading][0],
                        self.last_cell[1] + self.dirs[self.heading][1])
            new_value = self.sum_surrounding(new_cell)
            self.cells[new_cell] = new_value

            if self.heading in (0, 2) and abs(new_cell[0]) > self.max_[self.heading]:
                self.max_[self.heading] += 1
                self.heading += 1
            elif self.heading in (1, 3) and abs(new_cell[1]) > self.max_[self.heading]:
                self.max_[self.heading] += 1
                self.heading = (self.heading + 1) % len(self.dirs)
            self.last_cell = new_cell

        return new_value

    def sum_surrounding(self, coord: tuple):
        total = 0
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                cell = (coord[0] + x, coord[1] + y)
                if cell in self.cells:
                    total += self.cells[cell]
        return total


def test_p1_1():
    assert ms03_p1(1) == 0


def test_p1_2():
    assert ms03_p1(12) == 3


def test_p1_3():
    assert ms03_p1(23) == 2


def test_p1_4():
    assert ms03_p1(1024) == 31


def main():
    print(ms03_p1(325489))

    spiral = Spiral()

    last_cell = 0
    while last_cell < 325489:
        last_cell = spiral.add_cell()

    print(
        f"There are {len(spiral.cells)} entries, and the last one was {last_cell}")


if __name__ == '__main__':
    main()
