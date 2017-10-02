import copy

from Graph import Graph
from Graph import Edge
import numpy as np
from numpy import inf
import copy

class Solution(object):
    def __init__(self, val):
        if isinstance(val, Graph):
            self.g = val
            self.cost = 0
            self.visited = np.empty(shape=0, dtype = int)
            self.visited = np.append(self.visited, 0) #need to appear twice in the solution
            self.not_visited = np.arange(0,val.N)
            self.explored_nodes = 0
            self.created_nodes = 0
        elif isinstance(val, Solution):
            self.g = val.g
            self.cost = val.cost
            self.visited = val.visited
            self.not_visited = val.not_visited
            self.explored_nodes = val.explored_nodes
            self.created_nodes = val.created_nodes
        else:
            raise ValueError('you should give a graph or a solution')

    def add_edge(self, v, u):
        #do we need to check if v  is in the end of visited 
        self.cost = self.cost + self.g.get_edge(v,u).cost
        self.visited = np.append(self.visited, u)
        self.not_visited = np.delete(self.not_visited, np.argwhere(self.not_visited == u))

    def print(self):
        print("These are the visited cities in order", self.visited)
        print("Here is the cost for the trip",self.cost)
        print("number of explored nodes ",self.explored_nodes)
        print("number of created nodes ",self.created_nodes)

