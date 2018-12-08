import re

class Tasks:
    todo = set()
    started = set()
    done = set()
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

    # print ("Todo:", sorted(todo))
    # print ("Prereqs: ", requires)        


    def next_task(self):
        for task in sorted(self.todo):
            if task in self.done or task in self.started:
                continue
            else:
                ready = True
                if task in self.requires:
                    for prereq in self.requires[task]:
                        if prereq not in self.done:
                            ready = False
                if ready:
                    return task
        return None

    def start_task(self, task):
        """ Marks a task as started and returns the length of time it
        will take to complete.
        """
        self.started.add(task)
        return self.base_time + ord(task) - 64

    def finish_task(self, task):
        self.done.add(task)
        self.started.remove(task)


class Workers:
    busy_until = []
    working_on = []

    def __init__(self, worker_count):
        self.busy_until = [0 for i in range(worker_count)]
        self.working_on = ['' for i in range(worker_count)]

        
    def next_free_worker(self):
        return min(busy_until)

    
    def assign_worker(self, task):
        pass


    def move_clock(self, new_time):
        pass

    

    
def main():
    tasks = Tasks("day07input")


    

if __name__ == '__main__':
    main()
