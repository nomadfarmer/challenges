from timeit import default_timer

start = default_timer()

serial_number = 3628

def power(x, y):
    rack_id = x + 10
    res = y * rack_id
    res += serial_number
    res *= rack_id
    res //= 100
    res %= 10
    return res - 5

def make_board():
    board=[[0] * board_size for _ in range(board_size)]
    for y in range(board_size):
        for x in range(board_size):
            board[y][x] = power(x, y)
    return board

def corner_data():
    '''
     For each top-left corner, generate all possible wedges (top and left 
     side of a square). Store size (same as square side length) and score 
     for each wedge. Return data as the dict {pos:{size:score}}.
    '''
    toplefts = {}
    for y in range(board_size):
        for x in range(board_size):
            wedge = board[y][x]
            sizes = {1: wedge}
            for shift in range(1, board_size - max(x, y)):
                wedge += board[y+shift][x] + board[y][x+shift]
                sizes[shift + 1] = wedge
            toplefts[x,y] = sizes
    return toplefts

def find_best_corner():
    '''
    Use the data of top-left corners to find the best sum of wedges.
    By summing wedges from large to small, there's a shortcut:
    Whenever a sum of outer wedges is negative, stop summing. The inner
    wedges would be better off without, so this "chain of wedges" doesn't
    need to be calculated.
    '''
    total_best_score = 0
    for x, y in toplefts:
        for size in toplefts[x, y]:
            wedge_sum = toplefts[x, y][size]
            if wedge_sum < 0: #if the outermost wedge is negative, the inner square has a larger sum without it
                continue
            for step in range(1, size):
                wedge_sum += toplefts[x+step, y+step][size - step]
                if wedge_sum < 0: #same reasoning: inner square is better off without the negative outer layers
                    break
            else: #if the for loop finished, a full square has been calculated
                if wedge_sum > total_best_score:
                    total_best_score = wedge_sum
                    winner = x, y, size
    return winner

board_size = 300
board = make_board()
toplefts = corner_data()
winner = find_best_corner()
print(*winner,sep=',')
print(default_timer() - start)
