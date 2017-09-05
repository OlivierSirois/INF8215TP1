import copy

from Graph import Graph
from Graph import Edge
import numpy as np

class Solution(object):
    def __init__(self, s):
        if isinstance(s, Graph):
            self.g = s
            self.cost = 0
            self.visited = []
            self.not_visited = np.arange(0,s.N)
            self.edgecosts = s.costs
            
        elif isinstance(s, Solution):
            self.g = Solution.g
            self.cost = Solution.cost
            self.visited = Solution.visited
            self.not_visited = Solution.not_visited
        else:
            raise ValueError('you should give a graph or a solution')

    def add_edge(self, v, u):
        self.cost = self.cost + self.g.get_edge(v,u).cost
        self.visited.append(u)
        self.not_visited = np.delete(self.not_visited, u)

#    def print(self):
#        raise NotImplementedError()

First = Graph('N10.data')

Sol = Solution(First)

Sol.add_edge(0,7)
print(Sol.cost)
print(Sol.visited)
print(Sol.not_visited)

print(Sol.edgecosts)
#print(Sol.cost)

#print(Sol.visited)
#print(Sol.not_visited)
#print(Sol.g.costs)

#EXAMPLE MAP
print(list(map(lambda x:x.cost,Sol.g.get_sorted_edges())))
