ip = 0
part_2 = False
a, b, c, d, e = 0
# goto 17
e += 2  
e *= e
e *= 19
e *= 11
d += 2
d *= 22
d += 16
e += d
# ###
# d = 60
# e = 896

if part_2:
    # make d and e even bigger
    d = 10550400
    e += d # 10551296
    a = 0
# goto 1
b = 1
# line 2:
c = 1

# line 3:

d = b * c
if d == e: #line 4-5 --
    d = 1
    # line 7
    a += b
else:
    d = 0
    # line 6 -- goto 8
c += 1
if c > e:     #line 9, 10
    d = 1
    # skip a line to 12
else:
    d = 0
    # goto 3 -- Rewrite as a while e >= c: loop

# 12:
b += 1
if b > e:     # 13-14
    d = 1
    exit()
else:
    d = 0
    # goto 2
    
