from graph import Graph
from kruskal import Kruskal, UnionFind
from solution import Solution
import numpy as np
from numpy import inf
import copy
from time import time
import Queue as Q

SOURCE = 0

class Node(object):
    def __init__(self, v, sol):
        self.v = v
        self.solution = sol
        self.Kru = Kruskal(sol.g)
        
        cityvector = copy.deepcopy(self.solution.visited)
        cityvector.append(0)
                
        try:
            villeproche = np.amin(np.delete(self.solution.edgecosts[self.v,:], cityvector))
        except ValueError:
            villeproche = 0
        else:
            villeproche = np.amin(np.delete(self.solution.edgecosts[self.v,:], cityvector))

        try:
            orgtoville = np.amin(np.delete(self.solution.g.costs[0,:], cityvector))
        except ValueError:
            orgtoville = 0
        else:
            orgtoville = np.amin(np.delete(self.solution.g.costs[0,:], cityvector))
            
        self.heuristic_cost = self.Kru.getMSTCost(self.solution) + villeproche + orgtoville


        #self.heuristic_cost = self.Kru.getMSTCost(self.solution)

        #villeproche = np.amin(np.delete(self.solution.edgecosts[self.v,:], self.solution.visited))
        #print(self.solution.g.costs)
        #orgtoville = np.amin(np.delete(self.solution.g.costs[0, :], self.solution.visited))
        #print(orgtoville)
        
    def __lt__(self, other):  
        return isN2betterThanN1(other, self)
        
    def explore_node(self):
        #Returns all possible nodes connected to this one in a form of a list
        NextNodes = []
        if(len(self.solution.not_visited) == 1):
            nn = copy.deepcopy(Node(self.v, self.solution))
            nn.solution.add_edge(nn.v,0)
            nn.v = 0
            nn.update_heuristic_cost()
            NextNodes.append(nn)
        else:
            for i in self.solution.not_visited:
                if i != 0:
                    nn = copy.deepcopy(Node(self.v, self.solution))
                    nn.solution.add_edge(nn.v,i)
                    nn.v = i
                    nn.update_heuristic_cost()
                    NextNodes.append(nn)
        return NextNodes
    
    def update_heuristic_cost(self):
        #updates the cost of the heuristic for the Node, used in the explore_node method to update the heuristic cost before returning the new nodes
        cityvector = copy.deepcopy(self.solution.visited)
        cityvector.append(0)
        try:
            villeproche = np.amin(np.delete(self.solution.edgecosts[self.v,:], cityvector))
        except ValueError:
            villeproche = 0
        else:
            villeproche = np.amin(np.delete(self.solution.edgecosts[self.v,:], cityvector))

        try:
            orgtoville = np.amin(np.delete(self.solution.g.costs[0,:], cityvector))
        except ValueError:
            orgtoville = 0
        else:
            orgtoville = np.amin(np.delete(self.solution.g.costs[0,:], cityvector))
            
        self.heuristic_cost = self.Kru.getMSTCost(self.solution) + villeproche + orgtoville
        #self.heuristic_cost = 0     
        #print('ville la plus proche', villeproche)
        #print('closest to origin', orgtoville)
        #self.solution.print()
        
def main():
    g = Graph("N10.data")
    sol = Solution(g)
    start_node = Node(0, sol)
    nodes = Q.PriorityQueue()
    nodes.put(start_node)
    solutionfound = 0
    t1 = time()
    
    next_nodes = nodes.get();
    while(len(next_nodes.solution.not_visited) is not 0):
       new_nodes = next_nodes.explore_node()
       for i in range(0, len(new_nodes)): nodes.put(new_nodes[i])
       next_nodes = nodes.get()
    
    print('Solution found')
    print(next_nodes.solution.print_stuff())
    t2 = time()
    td = t2-t1
    print('Time difference: ', td)
 

def isN2betterThanN1(N1, N2):
    if (N1.solution.cost + N1.heuristic_cost > N2.solution.cost + N2.heuristic_cost): return True
    else: return False
    # if (N1.solution.cost > N2.solution.cost): return True
    # else: return False

if __name__ == '__main__': main()
