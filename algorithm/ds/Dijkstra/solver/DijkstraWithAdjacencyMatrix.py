
'''
https://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/
'''

class Graph():
    INF = 1 << 31

    def __init__(self, vertices):
        self.vertices = vertices
        self.matrix = [[0 for c in range(0, self.vertices)]
            , [0 for r in range(0, self.vertices)]]

        self.distances = [self.INF] * vertices
        self.spanning_tree = [False] * vertices

    def min_distances(self):
        print(self.distances)

    def __find_min_distance(self):
        min = self.INF
        min_vertex = 0
        for vertex in range(0, self.vertices):
            if self.distances[vertex] < min and not self.spanning_tree[vertex]:
                min, min_vertex = self.distances[vertex], vertex
        return min_vertex

    def shortest_path(self, source):
        # distancia entre o no fonte e ele mesmo eh 0 :)
        self.distances[source] = 0
        for v in range(0, self.vertices):
            min_vertex = self.__find_min_distance()
            self.spanning_tree[min_vertex] = True
            for k in range(0, self.vertices):
                new_distance = self.matrix[min_vertex][k] + self.distances[min_vertex]
                distance = self.distances[k]
                # existe um vertice entre min_vertex e k ?
                # k nao esta na arvore minima ?
                # a nova aresta adicionada a arvore tem peso menor que a antiga ?
                if self.matrix[min_vertex][k] > 0 \
                        and not self.spanning_tree[k] and new_distance < distance:
                    # atualiza a distancia
                    self.distances[k] = new_distance

        return


g = Graph(9)
g.matrix = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0]
    , [4, 0, 8, 0, 0, 0, 0, 11, 0]
    , [0, 8, 0, 7, 0, 4, 0, 0, 2]
    , [0, 0, 7, 0, 9, 14, 0, 0, 0]
    , [0, 0, 0, 9, 0, 10, 0, 0, 0]
    , [0, 0, 4, 14, 10, 0, 2, 0, 0]
    , [0, 0, 0, 0, 0, 2, 0, 1, 6]
    , [8, 11, 0, 0, 0, 0, 1, 0, 7]
    , [0, 0, 2, 0, 0, 0, 6, 7, 0]
];

g.shortest_path(0)
g.min_distances()

if __name__ == '__main__':
    pass
