import unittest

def findComponents(V, E):
    def dfs(vertex, graph, visited: set):
        visited.add(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                dfs(neighbour, graph, visited)

    # process the data from list to dict
    graph1 = {v: set() for v in V}
    for (edge1, edge2) in E:
        graph1[edge1].add(edge2)
        graph1[edge2].add(edge1)

    components = []
    remaining_vertices = set(V)

    while remaining_vertices:
        visited = set()
        dfs(next(iter(remaining_vertices)), graph1, visited)
        components.append(sorted(list(visited)))
        remaining_vertices.difference_update(visited)

    return components


class TestGraphComponents(unittest.TestCase):
    def test_testcase1(self):
        V = [1, 2, 3, 4, 5, 6, 7, 8]
        E = [(1, 2), (2, 3), (1, 3), (4, 5), (5, 6), (5, 7), (6, 7), (7, 8)]
        result = findComponents(V, E)
        expected = [[1, 2, 3], [4, 5, 6, 7, 8]]
        self.assertEqual(result, expected)

    def test_testcase2(self):
        V = [1, 2, 3, 4, 5]
        E = [(1, 2), (1, 3), (1, 4), (1, 5)]
        result = findComponents(V, E)
        expected = [[1, 2, 3, 4, 5]]
        self.assertEqual(result, expected)

    def test_testcase3(self):
        V = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        E = [(1, 2), (1, 3), (1, 8), (3, 7), (4, 5), (4, 6), (4, 9), (5, 6), (5, 9), (7, 8)]
        result = findComponents(V, E)
        expected = [[1, 2, 3, 7, 8], [4, 5, 6, 9]]
        self.assertEqual(result, expected)

    def test_testcase4(self):
        V = [1, 2, 3, 4, 5]
        E = []
        result = findComponents(V, E)
        expected = [[1], [2], [3], [4], [5]]
        self.assertEqual(result, expected)

    def test_testcase5(self):
        V = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        E = [(1,2), (2,3), (4,5), (7,8), (7,9), (9,10), (9,11), (9,12)]
        result = findComponents(V, E)
        expected = [[1, 2, 3], [4, 5], [6], [7, 8, 9, 10, 11, 12]]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
