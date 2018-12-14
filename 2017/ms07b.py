#/usr/bin/env python3
"""
Advent of Code 2017 - Day 07 - Recursive Circus
https://adventofcode.com/2017/day/7

Part 2:
As predicted, part two requires a tree. All children of a given parent
must weigh the same (including their own children). In the entire input,
one node's weight must be adjusted. Our job is to find the weight that
node needs to be adjusted by.
"""

import re

class Tree:
    nodes = {}
    root = ''
    
    def __init__(self, raw_data):
        child_nodes = set()
        all_nodes = set()
        
        for l in raw_data:
            names = re.findall(r'([a-z]+)', l)
            weight = int(re.findall(r'(\d+)', l)[0])
            if names[0] in self.nodes.keys():
                node = self.nodes[names[0]]
                node.weight = weight
            else:
                node = Node(names[0], weight)
                self.nodes[names[0]] = node
            all_nodes.add(names[0])

            children = {}
            for c in names[1:]:
                child_nodes.add(c)
                if c in self.nodes.keys():
                    child = self.nodes[c]
                else:
                    child = Node(c)
                    self.nodes[c] = child
                children[c] = child
            node.children = children

        root_name = list(child_nodes ^ all_nodes)[0]
        self.root = self.nodes[root_name]
        
                    
class Node:
    name = ''
    weight = 0
    children = {}
    def __init__(self, name, weight=0, children={}):
        self.name = name
        self.weight = weight
        if children:
            self.children = children

    def balanced(self):
        if not self.children:
            return True
        else:
            weights = set()
            for c in self.children.values():
                weights.add(c.total_weight())
            if len(weights) == 1:
                return True
            else:
                for c in self.children.values():
                    if not c.balanced():
                        return False
                names = []
                weights = []
                total_weights = []
                for c in self.children.values():
                    names.append(c.name)
                    weights.append(c.weight)
                    total_weights.append(c.total_weight())

                for i in total_weights:
                    if total_weights.count(i) > 1:
                        target = i
                    else:
                        bad_weight = i
                bad_prog = total_weights.index(bad_weight)
                new_weight = weights[bad_prog] + (target - bad_weight)
                print(f"Program {names[bad_prog]} should weigh {new_weight}.")
                return False

            
    def total_weight(self):
        w = self.weight
        for c in self.children.values():
            w += c.total_weight()
        return w

    
    def display(self, prefix=""):
        print(f"{prefix}{self.name}: {self.total_weight()}")
        for c in self.children.values():
            c.display("  " + prefix)


    def __repr__(self):
        return(f"{self.name}: {self.weight}, {len(self.children)}")
    
    
with open("ms07input") as f:
    raw_data = f.read().splitlines()

tree = Tree(raw_data)

# tree.root.display()
print("Bottom program: ", tree.root.name)
print("Total weight: ", tree.root.total_weight(), "\n")


tree.root.balanced()
