import re
from operator import itemgetter

def load_file(filename):
    with open(filename) as f:
        raw_lines = f.read().splitlines()

    parsed = []
    
    for line in raw_lines:
        m = re.match(r"#(\d+).*?(\d+),(\d+).*?(\d+)x(\d+)", line)
        parsed.append(tuple(map(int, m.groups())))
    
    return parsed


def part_a():
    claims = load_file("day03input")

    claimed_inches = set()
    double_claimed = set()
    
    for (cid, x, y, width, height) in claims:
        for i in range(x, x + width):
            for j in range(y, y+ height):
                if (i, j) in claimed_inches:
                    double_claimed.add((i, j))
                else:
                    claimed_inches.add((i, j))

    print(len(double_claimed))


def part_b():
    claims = load_file("day03input")

    claimed_inches = {}

    all_cids = set(map(itemgetter(0), claims))
    collided_cids = set()

    for (cid, x, y, width, height) in claims:
        for i in range(x, x + width):
            for j in range(y, y+ height):
                if (i, j) not in claimed_inches:
                    claimed_inches[(i, j)] = cid
                else:
                    collided_cids.add(cid)
                    collided_cids.add(claimed_inches[(i, j)])
                    
    print(all_cids ^ collided_cids)

    
if __name__ == '__main__':
    part_b()
