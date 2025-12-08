import numpy as np


class UnionFindBySize:
    def __init__(self, n):
        self.parents = np.arange(n, dtype="int")
        self.sizes = np.ones(n, dtype="int")
        self.n_components = n

    def find(self, u):
        if self.parents[u] != u:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union_sets(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return

        u_size = self.sizes[root_u]
        v_size = self.sizes[root_v]
        if u_size < v_size:
            self.parents[root_u] = root_v
            self.sizes[root_v] += u_size
        else:
            self.parents[root_v] = root_u
            self.sizes[root_u] += v_size
        self.n_components -= 1
