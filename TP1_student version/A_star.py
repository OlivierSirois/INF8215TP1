import queue as Q

from Graph import Graph
import Kruskal
from Solution import Solution

SOURCE = 0

class Node(object):
    def __init__(self, v, sol, heuristic_cost=0):
        self.v = [0]
        self.solution = sol
        self.heuristic_cost = None

    def explore_node(self, heap):
        raise NotImplementedError()


def main():
    g = Graph("N15.data")
    import Kruskal
    Kruskal.kruskal = Kruskal.Kruskal(g)
    heap = Q.PriorityQueue()



def isN2betterThanN1(N1, N2):
    raise NotImplementedError


if __name__ == '__main__':
    main()
