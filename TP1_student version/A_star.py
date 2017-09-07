import queue as Q

from Graph import Graph
import Kruskal
from Solution import Solution
import numpy as np
from numpy import inf
import copy

SOURCE = 0

class Node(object):
    def __init__(self, v, sol, heuristic_cost=0):
        self.v = v
        self.solution = sol
        self.heuristic_cost = None

    def explore_node(self):
        #Returns all possible nodes connected to this one in a form of a list
        NextCities = self.solution.edgecosts[self.v, :]
        NextNodes = []
        for i in range(0, len(NextCities)):
            NextNodes.append(copy.deepcopy(Node(self.v, self.solution, self.heuristic_cost)))
            NextNodes[i].solution.add_edge(NextNodes[i].v,i)
            NextNodes[i].v = i
            #print(NextNodes[i].solution.print())
            print('v=',NextNodes[i].v)
        return NextNodes 

        '''
        allcities = self.solution.edgecosts[self.v,:]
        possibilityvector = np.delete(allcities, self.solution.visited)
        possibilityvector = np.delete(possibilityvector, 0)
        try:
            NextDestinationCost = np.ndarray.min(possibilityvector)
        except ValueError:
            NextDestinationCost = self.solution.edgecosts[self.v,0]
            NextCity = 0
        else:
            NextDestinationCost = np.ndarray.min(possibilityvector)
            NextCity = int(np.argwhere(allcities == NextDestinationCost))
        self.solution.add_edge(self.v, NextCity)
        self.v = NextCity
        '''    
            
def main():
    g = Graph("N10.data")
    sol = Solution(g)
    Nstart = Node(0, sol)
    N1 = Nstart.explore_node()
    #N1[7].solution.print()
    
    Nusing = copy.deepcopy(Nstart)

    ''''''
    for i in range(0, g.N):
        Nnext = Nusing.explore_node()
        nextcost = []
        for j in range(0, len(Nnext)):
            nextcost.append(Nnext[j].solution.cost)
            print(nextcost[j])
        #THIS IS WHERE ADD THE HEURISTIC COST

        ##
        a = Nnext[0].solution.cost
        for j in range(0, len(Nnext)):
            print('not_visited',Nnext[j].solution.not_visited)
            print('j', j)
            #if (j in Nnext[j].solution.not_visited):
            print('cost', Nnext[j].solution.cost)
            print('a', a)
            if (a > Nnext[j].solution.cost):
    
                a = Nnext[j].solution.cost
                #print("a = ", a)
                index = j
                    #print("j = ", j)
        #nextnode = np.argwhere(np.amin(nextcost) == nextcost)

        Nusing = copy.deepcopy(Nnext[index])
        #Nusing.solution.print()
        

    



def isN2betterThanN1(N1, N2):
    raise NotImplementedError


if __name__ == '__main__':
    main()
'''import Kruskal
    Kruskal.kruskal = Kruskal.Kruskal(g)
    heap = Q.PriorityQueue()'''
