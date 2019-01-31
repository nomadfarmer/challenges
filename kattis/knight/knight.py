import sys
from copy import deepcopy
from itertools import product
from heapq import heappush, heappop


class Board:
    def __init__(self):
        self.last_move = 0
        self.moves = {}
        self.open_squares = set()
        self.rows = 0
        self.cols = 0
        self.row_len = []
        self.row_sum = []
        self.col_len = []
        self.col_sum = []
        self.magic_number = None

    def setup(self, b):
        self.rows = len(b)
        self.cols = len(b[0])
        self.row_len = [0] * self.rows
        self.row_sum = [0] * self.rows
        self.col_len = [0] * self.cols
        self.col_sum = [0] * self.cols
        for row in range(self.rows):
            for col in range(self.cols):
                if b[row][col] > 0:
                    self.moves[b[row][col]] = (row, col)
                    self.row_len[row] += 1
                    self.row_sum[row] += b[row][col]
                    self.col_len[col] += 1
                    self.col_sum[col] += b[row][col]
        if self.rows in self.row_len:
            self.magic_number = self.row_sum[self.row_len.index(self.rows)]
        elif self.cols in self.col_len:
            self.magic_number = self.col_sum[self.col_len.index(self.cols)]
        else:
            self.magic_number = None

        self.open_squares = set(product(range(self.rows), range(self.cols)))
        self.open_squares -= set(self.moves.values())
        for i in range(1, (self.rows * self.cols) + 1):
            if i + 1 not in self.moves:
                self.last_move = i
                break

    def legal_moves(self):
        """ Return a list of board objects with valid positions after
        this board's.
        A valid position has the next move and also:
        * If the move after the next move is on the board, it must share
          at least one move with the new move.
        * if we know our magic number, it must still be possible for this
          row to meet it (simple way: sum of the row/col so far plus smallest
          move left * empty spots must not exceed magic number.)
        """
        new_boards = []
        move = self.last_move + 1
        m_cands = knights_moves(self.moves[self.last_move], self.open_squares)
        next_move_on_board = None
        for i in range(move + 1, self.rows * self.cols + 1):
            if i in self.moves:
                next_move_on_board = i
                break
        if next_move_on_board:
            m_cands &= knights_moves(self.moves[next_move_on_board],
                                     self.open_squares,
                                     next_move_on_board - move)
        # following_move = move + 1
        # if following_move in self.moves:
        #     new_moves &= knights_moves(self.moves[following_move],
        #                                self.open_squares)
        for m in m_cands:
            min_row_sum = self.row_sum[
                m[0]] + move * (self.cols - self.row_len[m[0]])
            min_col_sum = self.col_sum[
                m[1]] + move * (self.rows - self.col_len[m[1]])
            if (self.row_len[m[0]] == self.cols - 1) \
               and (self.col_len[m[1]] == self.cols - 1) \
               and (min_row_sum != min_col_sum):
                continue
            if self.magic_number:
                if min_row_sum > self.magic_number \
                   or min_col_sum > self.magic_number:
                    continue
                elif self.cols - self.row_len[m[0]] == 1 \
                     and min_row_sum != self.magic_number:
                    continue
                elif self.rows - self.col_len[m[1]] == 1 \
                   and min_col_sum != self.magic_number:
                    continue

            # This board is worth checking, so build it and add it to our set
            new_b = deepcopy(self)
            new_b.moves[move] = m
            new_b.open_squares.remove(m)
            new_b.row_len[m[0]] += 1
            new_b.row_sum[m[0]] += move
            new_b.col_len[m[1]] += 1
            new_b.col_sum[m[1]] += move
            new_b.magic_number = self.magic_number
            if not new_b.magic_number:
                if new_b.row_len[m[0]] == new_b.cols:
                    new_b.magic_number = new_b.row_sum[m[0]]
                elif new_b.col_len[m[1]] == new_b.rows:
                    new_b.magic_number = new_b.col_sum[m[1]]

            for i in range(move, (self.rows * self.cols) + 1):
                if i + 1 not in new_b.moves:
                    new_b.last_move = i
                    break
            new_boards.append(new_b)
        return new_boards

    def show(self):
        b = [[0] * self.rows for x in range(self.cols)]

        for m, (row, col) in self.moves.items():
            b[row][col] = m

        for r in range(len(b)):
            for c in range(len(b[0])):
                if c == 0:
                    print(f"{b[r][c]:2}", end='')
                else:
                    print(f"{b[r][c]:3}", end='')
            print()

    def debug_show(self):
        self.show()

        print(self.last_move)
        print(len(self.moves), self.moves)
        print(len(self.open_squares), self.open_squares)


def knights_moves(starts, open_squares, n=1):
    offsets = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1),
               (2, 1))
    moves = set()
    if not isinstance(starts, set):
        starts = {starts}
    for c in starts:
        for o in offsets:
            m = (c[0] + o[0], c[1] + o[1])
            moves.add(m)
    if n == 1:
        return moves & open_squares
    else:
        return knights_moves(moves & open_squares, open_squares, n - 1)


b = sys.stdin.readlines()
for i in range(len(b)):
    b[i] = [int(x) for x in b[i].split()]

start = Board()
start.setup(b)
start.show()
os = set(product(range(8), repeat=2))
print(len(knights_moves((4, 4), os, 4) & knights_moves((4, 4), os, 64)))

exit()
tries = 0
q = []
heappush(q, (len(start.open_squares), tries, start))
while q:
    _, _, b = heappop(q)
    if not b.open_squares:
        b.show()
        break
    new_bs = b.legal_moves()
    for new_b in new_bs:
        tries += 1
        heappush(q, (len(new_b.open_squares), tries, new_b))
