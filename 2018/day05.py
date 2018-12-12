import re
from string import ascii_lowercase

def load_file(filename):
    with open(filename) as f:
        raw_lines = f.read().strip()

    return raw_lines


def part_a(polymer):
    """
    My first solution. Build a regex of all reactions and use re.sub()
    to strip them all out.
    """
    reactions = "(?:"

    for l in ascii_lowercase:
        reactions += l + l.upper() + "|" + l.upper() + l + "|"

    reactions = reactions[0:-1] + ")"
    
    poly_length = len(polymer)

    while True:        
        polymer = re.sub(reactions, '', polymer)
        if len(polymer) == poly_length:
            break
        else:
            poly_length = len(polymer)

    return len(polymer)


def part_a_rec(polymer):
    """
    A bonus attempt. I thought that maybe regex was slow, so I tried
    this recursive function. It's slower than the regex solution
    by a factor of 5.
    """
    skip = False
    new_poly = ''
    for i in range(len(polymer) - 1):
        if skip:
            skip = False
        elif abs(ord(polymer[i]) - ord(polymer[i + 1])) == 32:
            skip = True
        else:
            new_poly += polymer[i]

    if not skip:
        new_poly += polymer[-1]
        
    if len(new_poly) < len(polymer):
        return part_a_rec(new_poly)
    else:
        return len(new_poly)


def part_b(polymer):
    shortest = len(polymer)

    for c in ascii_lowercase:
        unit = '[' + c + '|' + c.upper() + ']'
        new_poly = re.sub(unit, '', polymer)
        new_poly_len = part_a(new_poly)
        if new_poly_len < shortest:
            shortest = new_poly_len

    return shortest


if __name__ == '__main__':
    print(part_a(polymer = load_file("day05input")))
    # print(part_a_rec(polymer = load_file("day05input")))
    # print(part_b(polymer = load_file("day05input")))

