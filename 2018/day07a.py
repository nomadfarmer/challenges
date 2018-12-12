import re

def load_file(filename):
    with open(filename) as f:
        raw_lines = f.read().splitlines()
    return raw_lines


def part_a():
    todo = set()
    done = set()
    requires = {}
    order = ''

    for l in load_file("day07input_fisk"):
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

    while len(done) < len(todo):
        for task in sorted(todo ^ done):
            if task in done:
                continue
            else:
                ready = True
                if task in requires:
                    for prereq in requires[task]:
                        if prereq not in done:
                            ready = False
                if ready:
                    order += task
                    done.add(task)
                    break

    print(order)
            

if __name__ == '__main__':
    part_a()
