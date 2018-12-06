import re

def load_file(filename):
    with open(filename) as f:
        raw_lines = f.read().splitlines()

    return sorted(raw_lines)


def part_a():
    log = load_file("day04input")

    guards = {}
    nap_start = -1
    current_guard = -1
    
    for line in log:
        if nap_start >= 0:
            m = re.search(r":(\d+)", line)
            nap_end = int(m.group(1))
            for i in range(nap_start, nap_end):
                guards[current_guard][i] += 1
            nap_start = -1
            continue
                          
        m = re.search(r":(\d+).*#(\d+)", line)

        if m:
            current_guard = m.group(2)
            if current_guard not in guards:
                guards[current_guard] = [0 for i in range(60)]
        else:
            m = re.search(r":(\d+)(?=.*falls)", line)
            nap_start = int(m.group(1))

    guard_total_sleep = {}
    for g, t in guards.items():
        guard_total_sleep[g] = sum(t)

    sleepiest_guard = 0
    most_slept = 0
    for g, t in guard_total_sleep.items():
        if t > most_slept:
            most_slept = t
            sleepiest_guard = g

    best_minute = guards[sleepiest_guard].index(max(guards[sleepiest_guard]))
    print(75 * "=")
    print("Strategy 1")
    print(75 * "-")
    print("Sleepiest guard: ".rjust(30), sleepiest_guard)
    print("Minutes slept: ".rjust(30), most_slept)
    print("Best minute: ".rjust(30), best_minute)
    print("Answer: ".rjust(30), best_minute * int(sleepiest_guard))

    print(75 * "=")

    most_slept = 0
    for g, s in guards.items():
        if max(s) > most_slept:
            sleepiest_guard = g
            most_slept = max(s)
            best_minute = s.index(max(s))

    print("Strategy 2")
    print(75 * "-")
    print("Most consistent guard: ".rjust(30), sleepiest_guard)
    print("Best minute: ".rjust(30), best_minute)
    print("Times slept in that minute: ".rjust(30), most_slept)
    print("Answer: ".rjust(30), best_minute * int(sleepiest_guard))

    print(75 * "=")


    
    # print(guards)
    # for guard in guards:
    #    print(guard, guards[guard])
    
    

def part_b():
    pass


if __name__ == '__main__':
    part_a()
