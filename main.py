import networkx as nx
import copy
import random


Graph = nx.complete_multipartite_graph(2,3,4) #задание графа - генератор

all_edges = list(nx.generate_edgelist(Graph, data = False))
edges = []
for edge in all_edges:
  u, v = edge.split()
  edges.append([int(u), int(v)])

nodes = list(Graph.nodes)
nx.draw(Graph,with_labels=True)


def contract(nodes, edges): #алгоритм
  while len(nodes) > 2:
    ind = random.randrange(0, len(edges))
    [u, v] = edges.pop(ind)
    nodes.remove(v)
    edge = []
    for i in range(len(edges)):
      if edges[i][0] == v:
        edges[i][0] = u
      elif edges[i][1] == v:
        edges[i][1] = u
      if edges[i][0] != edges[i][1]:
        edge.append(edges[i])
    edges = edge
  return nodes, edges
finalNodes, finalEdges = contract(nodes,edges)


print('Итоговые ребра:', finalEdges)
print('Итоговые вершины:', finalNodes)

gr = nx.Graph()
gr.add_edges_from(finalEdges)
nx.draw(gr)