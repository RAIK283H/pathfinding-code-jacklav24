import math
import unittest
import graph_data
import global_game_data
import pathing
import permutation
import f_w  
class TestPathFinding(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)
        
    def setUp(self):

        # Set target node for this test case
        global_game_data.target_node = [1,1,1,6,1,1,1,1,1,1,1,1]  # Target is node 1
        global_game_data.current_graph_index = 0
        

    def test_bfs_paths(self):
        self.setUp()
        global_game_data.current_graph_index = 0
        path = pathing.get_dfs_path()
        self.assertEqual(path, [1, 2])  
        global_game_data.current_graph_index = 3
        path = pathing.get_dfs_path()
        self.assertEqual(path, [1, 2, 3, 7, 6, 5, 4, 0, 1, 2, 3, 7, 11, 10, 9, 8, 12, 13, 14, 15])
    def test_dfs_path(self):
        self.setUp()
        path = pathing.get_bfs_path()
        self.assertEqual(path, [1,2])
        global_game_data.current_graph_index = 3
        path = pathing.get_bfs_path()
        self.assertEqual(path, [1,2,6,7,11,15])

    def test_sjt_permutations(self):
        perms = list(permutation.perm(3))
        expected = [[1, 2, 3], [1, 3, 2], [3, 1, 2], [3, 2, 1], [2, 3, 1]]
        self.assertEqual(perms, expected)

    def test_hamiltonian_cycle_detection(self):
        graph = [
            [(0,0), [1,2]],
            [(0,200), [0,3]],
            [(200,200), [0,3]],
            [(200,0), [1,2]]
        ]
        self.assertEqual(permutation.find_h_cycle(graph), -1)

    def test_valid_hamiltonian_cycle(self):
        graph = graph_data.graph_data[0]
        cycle = [1]
        self.assertTrue(permutation.is_valid_h_cycle(graph, cycle))

    def test_dijkstra_path(self):
        # Test dijkstra from start to target
        global_game_data.current_graph_index = 0
        path = pathing.get_dijkstra_path()
        self.assertEqual(path, [1, 2])  
        global_game_data.current_graph_index = 3
        path = pathing.get_dijkstra_path()
        self.assertEqual(path, [1,2,6,7,11,15])


    def test_fw(self):
        test_graph = [
            [(0, 0), [1, 2]],
            [(100, 100), [0, 2]],
            [(200, 200), [0, 1]],
        ]
        adj_list = [node[1] for node in test_graph]
        num_nodes = len(test_graph)
        graph_matrix = f_w.adj_list_to_matrix(adj_list, num_nodes)
        dist, next_node = f_w.fw(graph_matrix)

        self.assertEqual(dist[0][1], 1)
        self.assertEqual(dist[0][2], 1)
        self.assertEqual(dist[1][2], 1)

        path = f_w.remake_path(next_node, 0, 2)
        self.assertEqual(path, [0, 2])

    def test_fw_fail(self):
        graph = [
            [(0, 0), [1]],
            [(1, 1), [0]],
            [(2, 2), []],
        ]
        adj_list = [node[1] for node in graph]
        num_nodes = len(graph)
        graph_matrix = f_w.adj_list_to_matrix(adj_list, num_nodes)
        dist, next_node = f_w.fw(graph_matrix)

        self.assertEqual(dist[0][2], math.inf)
        self.assertEqual(
            f_w.remake_path(next_node, 0, 2), []
        )

    def test_fw_hard(self):
        graph = [
            [(0, 0), [1, 2]],
            [(1, 1), [0, 2, 3]],
            [(2, 2), [0, 1, 3]],
            [(3, 3), [1, 2]],
        ]
        adj_list = [node[1] for node in graph]
        num_nodes = len(graph)
        graph_matrix = f_w.adj_list_to_matrix(adj_list, num_nodes)
        dist, next_node = f_w.fw(graph_matrix)

        self.assertEqual(dist[0][3], 2)
        path = f_w.remake_path(next_node, 0, 3)
        self.assertEqual(
            path, [0, 1, 3]
        )

if __name__ == '__main__':
    unittest.main()
