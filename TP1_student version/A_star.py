import queue as Q

from Graph import Graph
from Kruskal import Kruskal, UnionFind
from Solution import Solution
import numpy as np
from numpy import inf
import copy
from time import time

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
        
    def explore_node(self):
        #Returns all possible nodes connected to this one in a form of a list
        NextCities = self.solution.edgecosts[self.v, :]
        NextNodes = []
        for i in range(0, len(NextCities)):
            NextNodes.append(copy.deepcopy(Node(self.v, self.solution)))
            NextNodes[i].solution.add_edge(NextNodes[i].v,i)
            NextNodes[i].v = i
            NextNodes[i].update_heuristic_cost()
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
        #print('ville la plus proche', villeproche)
        #print('closest to origin', orgtoville)
        #self.solution.print()

        
        
def main():
    g = Graph("N17.data")
    sol = Solution(g)
    Nstart = Node(0, sol)
    N1 = Nstart.explore_node()
    Nusing = copy.deepcopy(Nstart)
    Nodes = []
    Nodes.append(Nstart)
    solutionfound = 0
    t1 = time()
    while(solutionfound == 0):
        Nnext = Nodes[len(Nodes)-1]
        NewNodes = Nnext.explore_node()
        newcost = []
    
        for i in range(0, len(NewNodes)):
            newcost.append((NewNodes[i].solution.cost + NewNodes[i].heuristic_cost))


        index = np.argwhere(newcost == np.amax(newcost))
        a = NewNodes[int(index[0])]
        
        for j in range(0, len(NewNodes)):
            if ((j in Nnext.solution.not_visited) and ( j!= 0)):
                if (isN2betterThanN1(a, NewNodes[j])):
                    a = NewNodes[j]
                    index = j

            if ((len(Nnext.solution.not_visited) == 1) and ( j == 0 )):
                a = NewNodes[0]
                index = 0

        
        N = NewNodes[int(index)]
        Nodes.append(copy.deepcopy(N))
        #print(Nodes[len(Nodes)-1].solution.not_visited)
        if (len(Nodes[len(Nodes)-1].solution.not_visited) == 0):
            solutionfound = 1
            print('solution found!')
            print(len(Nodes), ' number of nodes explored')
            print(Nodes[len(Nodes)-1].solution.print())
            t2 = time()
            td = t2-t1
            print('time difference', td)
    print(Nodes[0].solution.g.costs)





def isN2betterThanN1(N1, N2):
    if ((N1.solution.cost + N1.heuristic_cost) > (N2.solution.cost + N2.heuristic_cost)):
        return True
    else:
        return False


if __name__ == '__main__':
    main()
