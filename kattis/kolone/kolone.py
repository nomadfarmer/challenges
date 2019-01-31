input()     # In python we don't care about the first line
x = input()
ants_going_right = set(x)
ants = x[::-1]

x = input()
ants_going_left = set(x)
ants += x

t = int(input())

for _ in range(t):
    skip = False
    for i in range(len(ants) - 1):
        if skip:
            skip = False
            continue
        if ants[i] in ants_going_right and ants[i + 1] in ants_going_left:
            ants = ants[:i] + ants[i + 1] + ants[i] + ants[i + 2:]
            skip = True
print(ants)
