import networkx as nx
import matplotlib.pyplot as plt
from graph_hw import Graph

# Создаем граф
graph = Graph()

# Добавляем узлы в граф
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)
graph.add_node(5)

# Добавляем ребра между узлами
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)
graph.add_edge(3, 5)
graph.add_edge(4, 5)

# Создаем объект NetworkX и добавляем узлы и рёбра из graph
nx_graph = nx.Graph()

# Добавляем узлы
for node in graph.nodes:
    nx_graph.add_node(node)

# Добавляем рёбра (на основе связей между узлами)
for node in graph.nodes:
    for child in graph.nodes[node].children:
        # Добавляем рёбра между узлами
        nx_graph.add_edge(node, child.value)

# Визуализация графа
plt.figure(figsize=(8, 6))
nx.draw(nx_graph, with_labels=True, node_color='lightgreen', node_size=1000, font_size=16, font_weight='bold')
plt.title("Визуализация графа на основе классов Node и Graph")
plt.show()