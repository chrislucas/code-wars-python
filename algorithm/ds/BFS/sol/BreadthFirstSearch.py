from collections import defaultdict

from queue import Queue

class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)

    def bfs(self, start):
        visiteds = [False] * len(self.adjacency_list)
        queue = Queue()
        queue.put(start)
        visiteds[start] = True
        while not queue.empty():
            current = queue.get()
            print(current)
            for element in self.adjacency_list[current]:
                if not visiteds[element]:
                    queue.put(element)
                    visiteds[element] = True

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)


g.bfs(0)


if __name__ == '__main__':
    pass
