import copy

from Graph import Graph


class Solution(object):
    def __init__(self, s):
        if isinstance(s, Graph):
            self.g = None
            self.cost = None
            self.visited = None
            self.not_visited = None
        elif isinstance(s, Solution):
            self.g = None
            self.cost = None
            self.visited = None
            self.not_visited = None
        else:
            raise ValueError('you should give a graph or a solution')

    def add_edge(self, v, u):
        raise NotImplementedError()

    def print(self):
        raise NotImplementedError()