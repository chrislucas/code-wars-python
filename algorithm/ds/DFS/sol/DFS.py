from collections import defaultdict


class Graph:
    def __init__(self, nodes):
        self.adjacency_list = defaultdict(list)
        self.visiteds = [False] * nodes

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)

    def helper_dfs(self, source):
        self.dfs(source)

    def dfs(self, source):
        self.visiteds[source] = True
        for e in self.adjacency_list[source]:
            print("From %d To %d" % (source, e))
            if not self.visiteds[e]:
                self.dfs(e)


g = Graph(5)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.helper_dfs(0)

if __name__ == '__main__':
    pass
