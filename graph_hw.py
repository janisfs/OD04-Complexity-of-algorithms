# Класс Node представляет собой узел графа
class Node:
    def __init__(self, value):
        # Инициализируем узел с заданным значением
        self.value = value
        # Инициализируем список детей узла
        self.children = []


# Класс Graph представляет собой граф
class Graph:
    def __init__(self):
        # Инициализируем граф с пустым словарем узлов
        self.nodes = {}


    # Метод add_node добавляет узел в граф
    def add_node(self, value):
        # Добавляем узел в словарь узлов графа
        self.nodes[value] = Node(value)


    # Метод add_edge добавляет ребро между двумя узлами графа
    def add_edge(self, node1, node2):
        # Если оба узла существуют в графе, добавляем ребро между ними
        if node1 in self.nodes and node2 in self.nodes:
            # Добавляем узел node2 в список детей узла node1
            self.nodes[node1].children.append(self.nodes[node2])
            # Добавляем узел node1 в список детей узла node2
            self.nodes[node2].children.append(self.nodes[node1])


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


# Для визуализации графа запустить файл main_graph.py