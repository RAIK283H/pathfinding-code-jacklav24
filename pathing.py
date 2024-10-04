import graph_data
import global_game_data
from numpy import random

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]


def get_random_path():
    path = []
    assert path == []
    def random_walk(current, end):
        if (current == end):
                return [current]
        else:
            # Access the current node's neighbors
            node = graph_data.graph_data[global_game_data.current_graph_index][current]
            neighbors = node[1]
            next_node = random.choice(neighbors)
            # Recursively walk to the end
            path = [current] + random_walk(next_node, end)  # Concatenate lists
            
        return path
    
    target = global_game_data.target_node[global_game_data.current_graph_index]
    end = len(graph_data.graph_data[global_game_data.current_graph_index]) - 1

    # Random walk from start to target and target to end
    start_to_target = random_walk(0, target)
    target_to_end = random_walk(target, end)

    path = start_to_target + target_to_end[1:] 
    assert (path[0] == 0) & (path[-1] == end)
    return path[1:]


def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
