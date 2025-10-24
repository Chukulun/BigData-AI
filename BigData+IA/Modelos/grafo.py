import networkx as nx
import random
import matplotlib.pyplot as plt

# grafo de n nodos donde la probabilidad de que un eje exista es de p
n = 5
G = nx.complete_graph(n)

for (u, v, w) in G.edges(data=True):
    w['weight'] = random.randint(0, 10)

edge_labels = nx.get_edge_attributes(G, 'weight')
label = nx.nodes(G)
nx.draw_shell(G, with_labels=True,)
nx.draw_networkx_edge_labels(G, nx.shell_layout(G), edge_labels= edge_labels)
plt.show()
