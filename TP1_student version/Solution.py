import copy

from Graph import Graph
from Graph import Edge
import numpy as np
from numpy import inf

class Solution(object):
    def __init__(self, s):
        if isinstance(s, Graph):
            self.g = s
            self.cost = 0
            self.visited = []
            self.not_visited = np.arange(0,s.N)
            self.edgecosts = s.costs
            self.edgecosts[self.edgecosts == 0] = inf
            self.sortedcosts = list(map(lambda x:x.cost, s.get_sorted_edges()))
            self.sortedsources = list(map(lambda x:x.source, s.get_sorted_edges()))
            self.sorteddestinations = list(map(lambda x:x.destination, s.get_sorted_edges()))
            
            
        elif isinstance(s, Solution):
            self.g = s.g
            self.cost = s.cost
            self.visited = s.visited
            self.not_visited = s.not_visited
            self.edgecosts = s.costs
            self.sortedcosts = s.sortedcosts
            self.sortedsources = s.sortedsources
            self.sorteddestination = s.sorteddestination
        else:
            raise ValueError('you should give a graph or a solution')

    def add_edge(self, v, u):
        self.cost = self.cost + self.g.get_edge(v,u).cost
        self.visited.append(u)
        self.not_visited = np.delete(self.not_visited, np.argwhere(self.not_visited == u))

    def print(self):
        print("These are the visited cities in order", self.visited)
        print("These are the ones left to visit in order", self.not_visited)
        print("Here is the cost for the trip",self.cost)

#First = Graph('N10.data')

#Sol = Solution(First)
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