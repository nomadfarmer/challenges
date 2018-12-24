import re
from operator import itemgetter
import itertools
# from tqdm import tqdm


def intersect(cube, nano):
    """cube: ((x, y, z), length) where xyz is the lower-left-far corner
    (that is, the corner with the lowest value in each dimension)
    nano: ((x, y, z), range)

    """
    verts = set()
    (x, y, z), r = nano
    for new_x in [x - r, x + r]:
        verts.add((new_x, y, z))
    for new_y in [y - r, y + r]:
        verts.add((x, new_y, z))
    for new_z in [z - r, z + r]:
        verts.add((x, y, new_z))
    
    


def dist(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1]) + abs(x[2] - y[2])


with open('input/day23') as f:
    raw_data = f.read().strip().splitlines()

nanos = {}

for l in raw_data:
    (x, y, z, r) = [int(i) for i in re.findall(r'(-?\d+)', l)]
    nanos[(x, y, z)] = r

strongest = max(nanos.items(), key=itemgetter(1))

in_range = 0

for n in nanos.keys():
    if dist(n, strongest[0]) <= strongest[1]:
        in_range += 1

print('strongest nano:', strongest)
print('Has', in_range, 'nanos in range')

print(len(nanos))

# verts = set()

# for (x, y, z), r in nanos.items():
#     # print(x, y, z, r)
#     for new_x in [x - r, x + r]:
#         verts.add((new_x, y, z))
#     for new_y in [y - r, y + r]:
#         verts.add((x, new_y, z))
#     for new_z in [z - r, z + r]:
#         verts.add((x, y, new_z))

# best_vert = ((0, 0, 0), 0)
# vert_scores = {}
# for v in verts:
#     in_range = 0
#     for ncoords, nr in nanos.items():
#         if dist(ncoords, v) <= nr:
#             in_range += 1
#     vert_scores[v] = in_range
#     if in_range > best_vert[1]:
#         best_vert = (v, in_range)
#         print(best_vert)
# # Best vert was
# # ((40149144, 48814154, 44059110), 872)
# # and submitting exactly that was too high




mins = []
maxes = []
for d in range(3):
    mins.append(min([k[d] for k in nanos.keys()]))
    maxes.append(max([k[d] for k in nanos.keys()]))

print(mins)
print(maxes)

largest_axis_length = max([abs(maxes[d] - mins[d]) for d in range(3)])
next_pow_4 = 1
while next_pow_4 < largest_axis_length:
    next_pow_4 *= 4

largest_axis_length = next_pow_4
print(largest_axis_length)
sr = largest_axis_length
granularity = 1
best_boxes = {(tuple(mins), granularity, '')}

done = False
while not done:
    boxes_to_check = tuple(best_boxes)
    best_boxes = set()
    if boxes_to_check[0][1] > largest_axis_length:
        print(boxes_to_check)
        done = True
        break

    for ((bx, by, bz), bg, ir) in boxes_to_check:
        granularity = bg * 4
        sr = largest_axis_length // granularity
        most_nanos = 0
        cand_boxes = set()
        print('Checking', (bx, by, bz), 'with gran', granularity, 'ir', ir)
        offsets = set([o * sr for o in range(5)])
        print(sr, offsets)

        for sub_x, sub_y, sub_z in itertools.product(offsets, repeat=3):
            print(sub_x, sub_y, sub_z)
            search_x = bx + sub_x
            search_y = by + sub_y
            search_z = bz + sub_z
            in_range = 0
            for (nx, ny, nz), nr in nanos.items():
                d_to_nano = dist((search_x, search_y, search_z), (nx, ny, nz))
                if d_to_nano <= sr + nr:
                    in_range += 1
            this_box = ((search_x - sr, search_y - sr, search_z - sr),
                        granularity, in_range)
            print('   sub', this_box)
            if in_range > most_nanos:
                most_nanos = in_range
                cand_boxes = {this_box}
            elif in_range == most_nanos:
                cand_boxes.add(this_box)
        best_boxes |= cand_boxes
print(best_boxes)
