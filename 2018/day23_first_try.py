import re
from operator import itemgetter
import itertools

# from tqdm import tqdm

fn = "input/day23"


def intersects(cube, nano):
    """cube: ((min_x, min_y, min_z), (max_x, max_y, max_z))
    nano: ((x, y, z), range)

    """
    verts = set()
    (x, y, z), r = nano
    (min_x, min_y, min_z), (max_x, max_y, max_z) = cube
    if min_x <= x <= max_x \
       and min_y <= y <= max_y \
       and min_z <= z <= max_z:
        return True

    for new_x in [x - r, x + r]:
        verts.add((new_x, y, z))
    for new_y in [y - r, y + r]:
        verts.add((x, new_y, z))
    for new_z in [z - r, z + r]:
        verts.add((x, y, new_z))

    for (x, y, z) in verts:
        if min_x <= x <= max_x \
           and min_y <= y <= max_y \
           and min_z <= z <= max_z:
            return True

    corners = itertools.product((min_x, max_x), (min_y, max_y), (min_z, max_z))
    for c in corners:
        if dist(c, nano[0]) <= nano[1]:
            return True

    return False


def dist(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1]) + abs(x[2] - y[2])


with open(fn) as f:
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

print('Nano count:', len(nanos))
print('strongest nano:', strongest)
print('Has', in_range, 'nanos in range')

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

# print(mins)
# print(maxes)

largest_axis_length = max([abs(maxes[d] - mins[d]) for d in range(3)])
print('Largest axis length:', largest_axis_length)
next_pow_2 = 1
while next_pow_2 < largest_axis_length:
    next_pow_2 *= 2
largest_axis_length = next_pow_2
print('  >>> next power of 2:', largest_axis_length)

granularity = 1
best_boxes = {(tuple(mins), granularity, '')}

done = False
while not done:
    boxes_to_check = tuple(best_boxes)
    best_boxes = set()
    most_nanos = 0
    # print('new boxes:', boxes_to_check)

    for ((bx, by, bz), bg, ir) in boxes_to_check:
        granularity = bg * 2
        box_length = largest_axis_length // granularity
        print(box_length)
        if box_length == 1:
            done = True

        cand_boxes = set()
        # print('Checking', (bx, by, bz), 'with gran', granularity, 'ir', ir)
        offsets = [0, box_length]
        # print(box_length, offsets)
        # print(list(itertools.product(offsets, repeat=3)))

        for sub_x, sub_y, sub_z in set(itertools.product(offsets, repeat=3)):
            # print(sub_x, sub_y, sub_z)
            box = ((bx + sub_x, by + sub_y, bz + sub_z),
                   (bx + sub_x + box_length - 1, by + sub_y + box_length - 1,
                    bz + sub_z + box_length - 1))

            in_range = 0
            for n in nanos.items():
                if intersects(box, n):
                    in_range += 1
            this_box = (box[0], granularity, in_range)
            # print('   sub', this_box)
            if in_range > most_nanos:
                most_nanos = in_range
                cand_boxes = {this_box}
            elif in_range == most_nanos:
                cand_boxes.add(this_box)
        best_boxes |= cand_boxes
    print(best_boxes)
    best_boxes = [b for b in best_boxes if b[2] == most_nanos]
    print(best_boxes)
print(best_boxes)
