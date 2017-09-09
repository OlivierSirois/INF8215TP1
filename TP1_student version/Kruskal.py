import numpy as np

kruskal = None


class UnionFind(object):
    def __init__(self, n):
        self.n = n
        self.parent = np.array(range(n))
        self.rnk = np.zeros(n)

    def reset(self):
        self.parent = np.array(range(self.n))
        self.rnk = np.zeros(self.n)

    def add(self, e):
        x = self.find(e.source)
        y = self.find(e.destination)

        if self.rnk[x] > self.rnk[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
        if self.rnk[x] == self.rnk[y]:
            self.rnk[y] += 1

    def makes_cycle(self, e):
        return self.find(e.source) == self.find(e.destination)

    def find(self, u):
        if u != self.parent[u]:
            return self.find(self.parent[u])
        else:
            return u


class Kruskal(object):
    def __init__(self, g):
        self.uf = UnionFind(g.N)
        self.g = g

    def getMSTCost(self, sol):
        #resetting values from UnionFind class so we don't have any remnants and only use the one
        #provided in our given solution
    
        self.uf.reset()
        Edges = sol.edges
        MST = []
        total = 0
    
        #adding edges currently in our sol to our unionfind class
        e = self.g.get_sorted_edges()

        for i in range(0, len(Edges)):
            self.uf.add(Edges[i])

        #calculating the total MST according to Kruskal's Algorithm
        for i in range(0, len(e)):
            if (not(self.uf.makes_cycle(e[i]))):
                self.uf.add(e[i])
                MST.append(e[i])
    
        for i in range(0, len(MST)):
            total = total + MST[i].cost
    
        return(total)
        
