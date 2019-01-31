PLAYERS = 419
MARBLES = 7216400

# PLAYERS = 9
# MARBLES = 25


class Ring:
    first_marble = None
    last_marble = None

    def add_marble(self, value, location):
        # print("Adding Marble: ", value)
        if self.last_marble:
            self.move(location)
            new_marble = Marble(value)
            new_marble.clockwise = self.last_marble.clockwise
            new_marble.widdershins = self.last_marble
            self.last_marble.clockwise = new_marble
            new_marble.clockwise.widdershins = new_marble
            self.last_marble = new_marble
        else:
            # print("It's the first marble")
            self.last_marble = Marble(value)
            self.last_marble.clockwise = self.last_marble
            self.last_marble.widdershins = self.last_marble
            self.first_marble = self.last_marble

    def __repr__(self):
        marbles = []
        marbles.append(self.first_marble)
        cm = self.first_marble.clockwise
        while cm != self.first_marble:
            marbles.append(cm)
            cm = cm.clockwise

        return str(self.last_marble.value) + str(marbles)

    def move(self, location):
        if location >= 0:
            for i in range(location):
                self.last_marble = self.last_marble.clockwise
        else:
            for i in range(abs(location)):
                self.last_marble = self.last_marble.widdershins

    def remove_marble(self, location):
        self.move(location)
        value = self.last_marble.value
        self.last_marble.clockwise.widdershins = self.last_marble.widdershins
        self.last_marble.widdershins.clockwise = self.last_marble.clockwise
        self.last_marble = self.last_marble.clockwise
        return value


class Marble:
    clockwise = None
    widdershins = None

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str((self.value, self.clockwise.value, self.widdershins.value))


ring = Ring()


# Our players will be 0 based. Remember to add one if it becomes important.
current_player = 0
scores = [0 for i in range(PLAYERS)]

for m in range(MARBLES + 1):
    # input()
    if m == 0 or m % 23 != 0:
        ring.add_marble(m, 1)
    else:
        scores[current_player] += m + ring.remove_marble(-7)
    current_player += 1
    if current_player == PLAYERS:
        current_player = 0
    # print(ring)
    # print(ring.last_marble)


print(max(scores))
