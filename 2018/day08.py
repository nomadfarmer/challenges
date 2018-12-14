class Node():
    def __init__(self, data, reverse=True):
        self.children = []
        self.metadata = []

        if reverse:
            data.reverse()

        children_count = int(data.pop())
        metadata_count = int(data.pop())

        for i in range(children_count):
            self.children.append(Node(data, reverse=False))

        self.metadata = [int(data.pop()) for i in range(metadata_count)]

    def total(self):
        answer = 0
        for c in self.children:
            answer += c.total()

        answer += sum(self.metadata)

        return answer

    def value(self):
        if not self.children:
            return sum(self.metadata)
        else:
            answer = 0
            for i in self.metadata:
                if i > 0 and i <= len(self.children):
                    answer += self.children[i - 1].value()
            return answer


def part_a():
    with open("day08input") as f:
        data = f.read().strip().split(" ")

    root = Node(data)
    print('Part 1 answer: ', root.total())
    print('Part 2 answer: ', root.value())


if __name__ == '__main__':
    part_a()
