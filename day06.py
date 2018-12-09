import string

ids = list(reversed(string.ascii_letters))

def get_id():
    return ids.pop()


class Point:
    def __init__(self, coords):
        self.id = get_id()
        self.infinite = False
        self.coords = coords
        self.area = 0


    def __repr__(self):
        return f"{self.id}: {str(self.coords)}, {self.infinite}\n"

    
    def x(self):
        return self.coords[0]

    
    def y(self):
        return self.coords[1]

    
    def distance(self, point_x):
        return abs(self.coords[0] - point_x[0]) + abs(self.coords[1] - point_x[1])
    

with open("day06input") as f:
    raw_data = f.read().strip().splitlines()


points = []
for l in raw_data:
    x, y = l.split(", ")
    points.append(Point((int(x), int(y))))

# print(points)

min_x = min([p.x() for p in points])
max_x = max([p.x() for p in points])
min_y = min([p.y() for p in points])
max_y = max([p.y() for p in points])

# print( len(points))

safe_area = 0

for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        distances = []
        for p in points:
            distances.append(p.distance((x, y)))
            closest = min(distances)
        if distances.count(closest) == 1:
            owner = points[distances.index(closest)]
            owner.area += 1
            if x in (min_x, max_x) or y in (min_y, max_y):
                owner.infinite = True
        if sum(distances) < 10000:
            safe_area += 1
        
max_area = 0
for p in points:
    if p.area > max_area and not p.infinite:
        max_area = p.area

print(points)
print("Largest non-infinite area: ", max_area)
print("Area closest to all points: ", safe_area)
