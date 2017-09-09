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
        self.heuristic_cost = self.Kru.getMSTCost(self.solution)
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
        self.heuristic_cost = self.Kru.getMSTCost(self.solution)
        
def main():
    g = Graph("N10.data")
    sol = Solution(g)
    Nstart = Node(0, sol)
    N1 = Nstart.explore_node()
    Nusing = copy.deepcopy(Nstart)
    Nodes = []
    Nodes.append(Nstart)
    solutionfound = 0
    '''
    sol1 = Solution(g)
    sol2 = Solution(g)
    sol3 = Solution(g)
    sol4 = Solution(g)
    sol5 = Solution(g)
    sol6 = Solution(g)
    sol7 = Solution(g)
    sol8 = Solution(g)
    sol9 = Solution(g)

    sol1.add_edge(0,1)
    sol2.add_edge(0,2)
    sol3.add_edge(0,3)
    sol4.add_edge(0,4)
    sol5.add_edge(0,5)
    sol6.add_edge(0,6)
    sol7.add_edge(0,7)
    sol8.add_edge(0,8)
    sol9.add_edge(0,9)

    Kru1 = Kruskal(g)
    Kru2 = Kruskal(g)
    Kru3 = Kruskal(g)
    Kru4 = Kruskal(g)
    Kru5 = Kruskal(g)
    Kru6 = Kruskal(g)
    Kru7 = Kruskal(g)
    Kru8 = Kruskal(g)
    Kru9 = Kruskal(g)


    print(Kru1.getMSTCost(sol1))
    print(Kru2.getMSTCost(sol2))
    print(Kru3.getMSTCost(sol3))
    print(Kru4.getMSTCost(sol4))
    print(Kru5.getMSTCost(sol5))
    print(Kru6.getMSTCost(sol6))
    print(Kru7.getMSTCost(sol7))
    print(Kru8.getMSTCost(sol8))
    print(Kru9.getMSTCost(sol9))

    for i in range(0, len(N1)):
        N1[i].solution.print()
        print(N1[i].heuristic_cost)
'''

 

    t1 = time()
    while(solutionfound == 0):
        Nnext = Nodes[len(Nodes)-1]
        NewNodes = Nnext.explore_node()
        newcost = []
    
        for i in range(0, len(NewNodes)):
            newcost.append((NewNodes[i].solution.cost + NewNodes[i].heuristic_cost))
        a = np.amax(newcost)
        index = np.argwhere(newcost == a)

        for j in range(0, len(NewNodes)):
            if ((j in Nnext.solution.not_visited) and ( j!= 0)):
                if (a > (NewNodes[j].solution.cost + NewNodes[j].heuristic_cost)):
                    a = NewNodes[j].solution.cost + NewNodes[j].heuristic_cost
                    index = j

            if ((len(Nnext.solution.not_visited) == 1) and ( j == 0 )):
                a = NewNodes[0].solution.cost + NewNodes[0].heuristic_cost
                index = 0


        N = NewNodes[int(index)]
        Nodes.append(copy.deepcopy(N))
        if (len(Nodes[len(Nodes)-1].solution.not_visited) == 0):
            solutionfound = 1
            print('solution found!')
            print(len(Nodes), ' number of nodes explored')
            print(Nodes[len(Nodes)-1].solution.print())
            t2 = time()
            td = t2-t1
            print('time difference', td) 
    

def isN2betterThanN1(N1, N2):
    if ((N1.solution.cost + N1.heuristic_cost) > (N2.solution.cost + N2.heuristic_cost)):
        return True
    else:
        return False


if __name__ == '__main__':
    main()
'''import Kruskal
    Kruskal.kruskal = Kruskal.Kruskal(g)
    heap = Q.PriorityQueue()'''
