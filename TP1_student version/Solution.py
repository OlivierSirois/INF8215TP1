import copy

from Graph import Graph
from Graph import Edge
import numpy as np
from numpy import inf
import copy

class Solution(object):
    def __init__(self, s):
        if isinstance(s, Graph):
            self.g = s
            self.cost = 0
            self.visited = []
            self.not_visited = np.arange(0,s.N)
            self.edgecosts = copy.deepcopy(s.costs)
            self.edgecosts[self.edgecosts == 0] = inf
            self.edges = []
        elif isinstance(s, Solution):
            self.g = s.g
            self.cost = s.cost
            self.visited = s.visited
            self.not_visited = s.not_visited
            self.edgecosts = s.costs
            self.edges = s.edges
        else:
            raise ValueError('you should give a graph or a solution')

    def add_edge(self, v, u):
        self.cost = self.cost + self.g.get_edge(v,u).cost
        self.visited.append(u)
        self.not_visited = np.delete(self.not_visited, np.argwhere(self.not_visited == u))
        self.edges.append(Edge(v,u, self.g.get_edge(v,u).cost))

    def print(self):
        print("These are the visited cities in order", self.visited)
        print("These are the ones left to visit in order", self.not_visited)
        print("Here is the cost for the trip",self.cost)

'''
#Sol.add_edge(0,7)
print(Sol.cost)
print(Sol.visited)
print(Sol.not_visited)

print(Sol.edgecosts)
#print(Sol.cost)

#print(Sol.visited)
#print(Sol.not_visited)
#print(Sol.g.costs)

#EXAMPLE MAP
print(Sol.sortedcosts)
print(Sol.sortedsources)
print(Sol.sorteddestination)
'''
