import re


class Tasks:
    todo = set()
    started = set()
    #    done = set()
    requires = {}
    base_time = 60

    def __init__(self, filename):
        with open(filename) as f:
            raw_lines = f.read().splitlines()

        for l in raw_lines:
            m = re.search(r"(\b[A-Z]\b).*(\b[A-Z]\b)", l)
            g = m.groups()
            self.todo.add(g[0])
            self.todo.add(g[1])
            if g[1] in self.requires:
                self.requires[g[1]].append(g[0])
            else:
                self.requires[g[1]] = [g[0]]

    def next_task(self):
        for task in sorted(self.todo):
            if task in self.started:
                continue
            else:
                ready = True
                if task in self.requires:
                    for prereq in self.requires[task]:
                        if prereq in self.todo or prereq in self.started:
                            ready = False
                if ready:
                    return task
        return None

    def start_task(self, task):
        """ Marks a task as started and returns the length of time it
        will take to complete.
        """
        self.started.add(task)
        self.todo.remove(task)
        return self.base_time + ord(task) - 64

    def finish_task(self, task):
        self.started.remove(task)


class Workers:
    busy_until = []
    working_on = []

    def __init__(self, worker_count):
        self.busy_until = [0 for i in range(worker_count)]
        self.working_on = ['' for i in range(worker_count)]

    def next_free_worker(self):
        return min(self.busy_until)

    def free_worker(self):
        try:
            self.busy_until.index(0)
        except ValueError:
            return False

        return True

    def assign_worker(self, task_d, task, time):
        free_worker = self.busy_until.index(0)
        self.busy_until[free_worker] = task_d.start_task(task) + time
        self.working_on[free_worker] = task

    def move_clock(self, task_d):
        times = set(self.busy_until)
        if 0 in times:
            times = times ^ {0}
        new_time = min(times)

        for w in range(len(self.busy_until)):
            if self.busy_until[w] and self.busy_until[w] <= new_time:
                task_d.finish_task(self.working_on[w])
                self.busy_until[w] = 0
                self.working_on[w] = ''
        return new_time


def main():
    task_d = Tasks("input/day07_s")
    workers = Workers(5)
    time = 0

    while len(task_d.todo):
        next_task = task_d.next_task()
        if next_task and workers.free_worker():
            workers.assign_worker(task_d, next_task, time)
        else:
            time = workers.move_clock(task_d)

    print(max(workers.busy_until))


if __name__ == '__main__':
    main()
