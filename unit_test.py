import math
import unittest
import graph_data
import global_game_data
import pathing
import permutation
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
        # Set up a sample graph for testing
        self.original_graph_data = graph_data.graph_data
        self.original_game_data = global_game_data
        
        
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


if __name__ == '__main__':
    unittest.main()
