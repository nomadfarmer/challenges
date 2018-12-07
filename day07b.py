import re

todo = set()
started = set()
done = set()
requires = {}
order = ''


def load_file(filename):
    with open(filename) as f:
        raw_lines = f.read().splitlines()
    return raw_lines


def init():
    for l in load_file("day07input"):
        m = re.search(r"(\b[A-Z]\b).*(\b[A-Z]\b)", l)
        g = m.groups()
        todo.add(g[0])
        todo.add(g[1])
        if g[1] in requires:
            requires[g[1]].append(g[0])
        else:
            requires[g[1]] = [g[0]]

    # print ("Todo:", sorted(todo))
    # print ("Prereqs: ", requires)        


def next_task():
    for task in sorted(todo):
        if task in done or task in started:
            continue
        else:
            ready = True
            if task in requires:
                for prereq in requires[task]:
                    if prereq not in done:
                        ready = False
            if ready:
                return task
    return None

def main():
    init()
    print(next_task())
    

if __name__ == '__main__':
    main()
