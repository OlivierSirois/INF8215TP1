import queue as Q

from Graph import Graph
from Kruskal import Kruskal, UnionFind
from Solution import Solution
import numpy as np
from numpy import inf
import copy
from time import time
import queue as Q

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
    g = Graph("N15.data")
    sol = Solution(g)
    Nstart = Node(0, sol)
    Nodes = Q.PriorityQueue()
    Nodes.put(Nstart)
    solutionfound = 0
    t1 = time()
    explored = 0
    created = 0
    while(solutionfound == 0):
        Nnext = Nodes.get(); # get the node with least A* cost        
        explored = explored+1 
       
        if (len(Nnext.solution.not_visited) == 0):
            solutionfound = 1
            Nnext.solution.created_nodes = created 
            Nnext.solution.explored_nodes = explored
            print('solution found!')
            print(Nnext.solution.print())
            t2 = time()
            td = t2-t1
            print('time difference', td)        
        else:
            NewNodes = Nnext.explore_node()
            created = created + len(NewNodes)
            sol.created_nodes =sol.created_nodes+ len(NewNodes)
            for i in range(0, len(NewNodes)):
                #print("adding node at", NewNodes[i].v,"and cost", NewNodes[i].solution.cost + NewNodes[i].heuristic_cost)
                Nodes.put(NewNodes[i])

        # Nodes should be using a high priority queue not just an array ...        
        
        #print(Nodes[len(Nodes)-1].solution.not_visited)
       
    #print(Nodes[0].solution.g.costs)


def isN2betterThanN1(N1, N2):
    if ((N1.solution.cost + N1.heuristic_cost) > (N2.solution.cost + N2.heuristic_cost)):
        return True
    else:
        return False


if __name__ == '__main__':
    main()
