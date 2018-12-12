from collections import deque

def marble_game(players, marbles):
    ring = deque()
    scores = [0] * players
    cur_player = 0

    for m in range(marbles + 1):
        if m == 0 or m % 23 != 0:
            ring.rotate(-1)
            ring.append(m)
        else:
            ring.rotate(7)
            scores[cur_player] += ring.pop() + m
            ring.rotate(-1)
        cur_player = (cur_player + 1) % players
        
    return max(scores)


assert marble_game(9, 25) == 32
assert marble_game(10, 1618) == 8317
assert marble_game(13, 7999) == 146373
assert marble_game(17, 1104) == 2764
assert marble_game(21, 6111) == 54718
assert marble_game(30, 5807) == 37305

print(marble_game(419, 72164))
print(marble_game(419, 7216400))
