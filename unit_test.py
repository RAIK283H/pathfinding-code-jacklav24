import math
import unittest
import graph_data
import global_game_data
import pathing
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
        
if __name__ == '__main__':
    unittest.main()
