#!python3
ans = 1
line = input()
for option in line.split():
    ans *= int(option)

print(ans)
