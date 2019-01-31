#!/usr/bin/env python3
import sys

"""
Given n amount of bricks, you have to see how many possible staircases you can
make. Every brick must be used, and every level of the staircase must be lower
than the level before it.

I spent an hour just constructing staircases on paper looking for patterns.

First, algorithm I automatically used is this:
Use all the bricks. (e.g., 9)
Use all the bricks but one (e.g. 8, 1)
Use one fewer for the highest level (e.g. 7, 2)
''   ''   ''                        (6, 3)
Now, here's where it gets interesting. There are two ways we can use 3 legally.

Because I started with 1, then 2, etc... I could always look up how many
mini-staircases could be made with the max height of current-1.

The first algorithm that makes sense to me is to do as I just did on paper, and
build all smaller staircases on the way to finding our ultimate answer. For each
number of bricks we will store the number of ways it can be built, at each maximum
height (If we have 9 bricks left, but the previous level was 6, how many ways can
we use them?)

I will build this iteratively first, although presumably we will spend time
calculating many permutations that won't exist in our actual target. I predict
that a recursive strategy (keeping a dict of previously calculated answers) will
ultimately be more efficient.

Stored data will be in a dict of dicts called perms[bricks][max_height].
e.g. perms[9][5] will store the number of stairs that can be built with 9
bricks such that the heighest level is 5 or less.
"""
def build_stairs(n):
    perms = {0: {0: 1},          # Saved permutations. Loading it with base
             1: {1: 1},          # cases up to 2.
             2: {2: 1}}
    if n in perms:
        return 1                 # Or perms[n][n], which is closer
                                 # to what a recursive algorithm would have.

    for total_bricks in range(3, n+1):
        current_perms = {}
        for top_stair in range(total_bricks, 0, -1):
            second_stair_bricks = total_bricks - top_stair
            # second row must be lower than the top row:
            max_height = top_stair - 1

            if max_height >= second_stair_bricks:
                # all_second_perms = perms[second_stair_bricks][max(perms[second_stair_bricks])]
                # current_perms[top_stair] = all_second_perms
                current_perms[top_stair] = perms[second_stair_bricks][second_stair_bricks]
            elif max_height in perms[second_stair_bricks]:
                current_perms[top_stair] = perms[second_stair_bricks][max_height]
            else:
                # we've reached the point where you can't use all of the bricks
                # after making the top stair too low.
                break
        # flatten current_perms:
        # current_perms should have the specific number at each height. We want
        # them cumulative -- e.g., perms[16][16] should include all possible
        # stairs with 16 bricks.
        perms[total_bricks] = {}
        heights = sorted(current_perms.keys())
        total_perms = 0
        for h in heights:
            total_perms += current_perms[h]
            perms[total_bricks][h] = total_perms
    print("Len(perms): ", len(perms))
    print("perms size for n = " + str(n) + " is : " + str(sys.getsizeof(perms)))
    return perms[n][n]

def test_build_stairs_0_to_6():
    answers = {0: 1,
               1: 1,
               2: 1,
               3: 2,
               4: 2,
               5: 3,
               6: 4}
    for t in answers.keys():
        assert(build_stairs(t) == answers[t])

# def test_build_stairs_10():
#     assert(build_stairs(10) == 10)
# 
# def test_build_stairs_15():
#     assert(build_stairs(15) == 27)
# 
# def test_build_stairs_20():
#     assert(build_stairs(20) == 64)
# 
# def test_build_stairs_30():
#     assert(build_stairs(30) == 296)
# 
# def test_build_stairs_40():
#     assert(build_stairs(40) == 1113)
# 
#def test_build_stairs_50():
#    assert(build_stairs(50) == 3658)
#
#def test_build_stairs_60():
#    assert(build_stairs(60) == 10880)
#
#def test_build_stairs_70():
#    assert(build_stairs(70) == 29927)
#
#def test_build_stairs_80():
#    assert(build_stairs(80) == 77312)
#
#def test_build_stairs_90():
#    assert(build_stairs(90) == 189586)
#
#def test_build_stairs_100():
#    assert(build_stairs(100) == 444793)
#
#def test_build_stairs_125():
#    assert(build_stairs(125) == 3207086)
#
#def test_build_stairs_150():
#    assert(build_stairs(150) == 19406016)
#
#def test_build_stairs_175():
#    assert(build_stairs(175) == 102614114)
#
#def test_build_stairs_200():
#    assert(build_stairs(200) == 487067746)
#
#def test_build_stairs_300():
#    assert(build_stairs(300) == 114872472064)
#
#def test_build_stairs_400():
#    assert(build_stairs(400) == 11962163400706)
#
#def test_build_stairs_500():
#    assert(build_stairs(500) == 732986521245024)
#
#def test_build_stairs_750():
#    assert(build_stairs(750) == 4923988648388880384)
#
#def test_build_stairs_1000():
#    assert(build_stairs(1000) == 8635565795744155161506)
#
def main():
#    build_stairs(200)
#    build_stairs(1000)
    print (build_stairs(4437))

if __name__ == "__main__":
    main()
def test_build_stairs_5000():
    assert(build_stairs(5000) == 15988884521431077020247618131907553242282546626679512)
