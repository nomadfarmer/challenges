truth_table = {True:1, False:0}
r0, r1, r2, r3, r4, r5 = [0, 0, 0, 0, 0, 0]

while 123 & 456 != 72:
    """ Actual code...
    r3 = 123
    r3 &= 456
    r3 = truth_table[3 == 72]
    ip += r3 # Skip next line if r3 equaled 72
    ip = 0
    """
    pass

# line 5 -- code starts for real
r3 = 0
first = True
while not first and r3 != r0:
    first = False
    r1 = r3 | 65536  #        10000000000000000 # Just 17th bit
    r3 = 14906355    # 111000110111001111110011
    
    #line 8 (from 
    r4 = r1 & 255    # 255:            11111111
    r3 += r4         # 0 at this point
    r3 &= 16777215   # 111111111111111111111111 -- 24 bits on
    r3 *= 65899      #        10000000101101011 -- 17 bits

    # line 13
    if r1 <= 256:     # into r4
        r4 = 0
        r2 = r4 + 1
        r2 *= 256
        if r2 > r1:   # into r2
            r1 = r4
            # goto line 8
if r3 == r0:
    exit()
else:
    goto line 6

