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
        self.solution = Solution(sol)
        self.Kru = Kruskal(sol.g)
        
    def __lt__(self, other):  
        return isN2betterThanN1(other, self)
        
    def explore_node(self):
        #Returns all possible nodes connected to this one in a form of a list
        NextNodes = []
        if(len(self.solution.not_visited) == 1): #if the only not visited city is 0, then we can add it
            nn = Node(self.v, self.solution)
            nn.solution.add_edge(nn.v,0)
            nn.v = 0
            nn.update_heuristic_cost()
            NextNodes.append(nn)
        else:
            for i in self.solution.not_visited: #explore the non-visited cities and create nodes
                if i != 0:          #not explore the city 0
                    nn = Node(self.v, self.solution)
                    nn.solution.add_edge(nn.v,i)
                    nn.v = i
                    nn.update_heuristic_cost()
                    NextNodes.append(nn)
        return NextNodes
        
    def update_heuristic_cost(self):
        #updates the cost of the heuristic for the Node, used in the explore_node method to update the heuristic cost before returning the new nodes                 
        #
        if(len(self.solution.not_visited) == 0):  #if solution is found , MST = 0
           villeproche = 0
           orgtoville = 0
           mstCost = 0
        elif(len(self.solution.not_visited) == 1): #if the only city left if 0
            villeproche = 0
            orgtoville = self.solution.g.costs[0, self.v]
            mstCost = 0
        else:         #lower bound 
           costOfNonVistedWithoutZero = self.solution.g.costs[:,np.delete(self.solution.not_visited, 0)]
           orgtoville = np.amin(costOfNonVistedWithoutZero[0, :])
           villeproche = np.amin(costOfNonVistedWithoutZero[self.v, :])
           mstCost = self.Kru.getMSTCost(self.solution) 
        # different addition just to run program with diferent heuristic to have the result 
        self.heuristic_cost = 0
        self.heuristic_cost = self.heuristic_cost + mstCost  #get only the cost heuristic            
        self.heuristic_cost = self.heuristic_cost + villeproche
        self.heuristic_cost = self.heuristic_cost + orgtoville        
        
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
            print('time difference (s)', td)        
        else:
            NewNodes = Nnext.explore_node()
            created = created + len(NewNodes)
            sol.created_nodes =sol.created_nodes+ len(NewNodes)
            for i in range(0, len(NewNodes)):
                #print("adding node at", NewNodes[i].v,"and cost", NewNodes[i].solution.cost + NewNodes[i].heuristic_cost)
                Nodes.put(NewNodes[i])



def isN2betterThanN1(N1, N2):
    if ((N1.solution.cost + N1.heuristic_cost) > (N2.solution.cost + N2.heuristic_cost)):
        return True
    else:
        return False


if __name__ == '__main__':
    main()
