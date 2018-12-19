"""
I read the mock assembler code by hand... re-interpreted comparisons
and jumps to while loops, then for loops, then recognized what we're
actually trying to accomplish.
"""


# part_2 = False
# a = b = c = d = e = 0
# d = 60
# e = 896

# if part_2:
#     # make d and e even bigger
#     d = 10550400
#     e += d # 10551296
#     a = 0
# # goto 1
# b = 1
# while e >= b:
#     c = 1
#     while e >= c:
#         d = b * c
#         if d == e:
#             a += b
#         c += 1
#     b += 1

# print(a)

# # Rewritten with for loops
# a = 0
# e = 10551296
# for b in range(1, e + 1):
#     for c in range(1, e + 1):
#         if b * c == e:
#             a += b

# # Add b to a if it is a factor of e... so
# # if e % b == 0: a += b

a = 0
e = 10551296
# e = 896
for b in range(1, e + 1):
    if e % b == 0:
        a += b
        print(a)
