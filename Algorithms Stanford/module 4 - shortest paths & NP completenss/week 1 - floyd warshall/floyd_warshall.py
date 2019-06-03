import networkx as nx
import numpy as np


class all_pairs_shortest_path:

    def __init__(self, text):

        f = open(text)

        lis = [tuple(map(int, x.split())) for x in f if x.strip()]

        self.listofEdges = lis

        G = nx.DiGraph()
        G.add_weighted_edges_from(lis)

        self.G = G

    def ShortestPathsMatrix(self):
        mat = nx.floyd_warshall_numpy(self.G)

        min_distance = np.min(mat)

        if abs(min_distance) > self.G.number_of_edges() * np.max([x[2] for x in self.listofEdges]):
            return 'Graph has a negative cycle'

        return min_distance


results = {}
G = {}

for i in range(1, 4):
    G[i] = all_pairs_shortest_path('g{}.txt'.format(i))
    results[i] = G[i].ShortestPathsMatrix()
    print(results[i])







