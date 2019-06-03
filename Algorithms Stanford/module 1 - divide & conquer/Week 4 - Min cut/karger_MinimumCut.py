import networkx as nx
import random
import secrets


G = nx.read_adjlist('kargerMinCut.txt', create_using=nx.MultiGraph(), nodetype=int)

print(nx.info(G))


def contracted_nodes(G, u, v, self_loops):
    # modified version of contract_nodes() in the networkx source code

    new_edges = ((u, w, d) for x, w, d in G.edges(v, data=True) if self_loops or w != u)

    new = [n for n in new_edges]

    v_data = G.node[v]
    G.remove_node(v)
    G.add_edges_from(new)
    if 'contraction' in G.node[u]:
        G.node[u]['contraction'][v] = v_data
    else:
        G.node[u]['contraction'] = {v: v_data}






def randContraction(G):
    while G.number_of_nodes() > 2:

        u, v = secrets.choice(list(G.edges()))

        contracted_nodes(G, u, v, self_loops=False)

    return int(G.number_of_edges()/2)



rand_min_cut = randContraction(G)
print('\nMinimum cut is: {}'.format(rand_min_cut))
