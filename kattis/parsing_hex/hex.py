import sys
import re

inp = sys.stdin.readlines()

hex_strs = []

for l in inp:
    hex_strs += re.findall(r"(0[xX][0-9a-fA-F]{1,8})", l)

for h in hex_strs:
    print(h.lower(), int(h, 16))
