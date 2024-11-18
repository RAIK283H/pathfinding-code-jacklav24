import graph_data
import global_game_data
from numpy import random
from collections import deque

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
            path = [current] + random_walk(next_node, end) 
            
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
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    path = []
    visited = set()
    
    target = global_game_data.target_node[global_game_data.current_graph_index]
    end = len(graph_data.graph_data[global_game_data.current_graph_index]) - 1

    start_to_target = dfs(0, target, set())
    target_to_end = dfs(target, end, visited)

    path = start_to_target + target_to_end[1:]
    for i in range(len(start_to_target) - 1):
        assert(start_to_target[i + 1] in graph[start_to_target[i]][1])
    for i in range(len(target_to_end) - 1):
        assert(target_to_end[i + 1] in graph[target_to_end[i]][1])
    assert (path[0] == 0) & (path[-1] == end)
    assert target in path
    return path[1:]  
def dfs(current, end, visited):
        if current == end:
            return [current]

        visited.add(current)
        node = graph_data.graph_data[global_game_data.current_graph_index][current]
        neighbors = node[1]
        
        for next_node in neighbors:
            if next_node not in visited:
                result = dfs(next_node, end, visited)
                if result:
                    return [current] + result
        return None
    

def get_bfs_path():
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    target = global_game_data.target_node[global_game_data.current_graph_index]
    end = len(graph_data.graph_data[global_game_data.current_graph_index]) - 1


    start_to_target = bfs(0, target)

    target_to_end = bfs(target, end)

    path = start_to_target + target_to_end[1:]

    for i in range(len(start_to_target) - 1):
        assert(start_to_target[i + 1] in graph[start_to_target[i]][1])
    for i in range(len(target_to_end) - 1):
        assert(target_to_end[i + 1] in graph[target_to_end[i]][1])
    assert (path[0] == 0) & (path[-1] == end)
    assert target in path

    return path[1:]  
def bfs(start, end):
        queue = deque([start])  
        visited = set([start])  
        parent = {start: None} 

        while queue:
            current = queue.popleft()
            if current == end:
                path = []
                while current is not None:
                    path.append(current)
                    current = parent[current]
                return path[::-1]


            node = graph_data.graph_data[global_game_data.current_graph_index][current]
            neighbors = node[1]
            for next_node in neighbors:
                if next_node not in visited:
                    queue.append(next_node)
                    visited.add(next_node)  
                    parent[next_node] = current  
        return None  # return None if no path is found


def get_dijkstra_path():
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    target = global_game_data.target_node[global_game_data.current_graph_index]
    end = len(graph_data.graph_data[global_game_data.current_graph_index]) - 1

    start_to_target = dijkstra(0, target)
    target_to_end = dijkstra(target, end)
    path = start_to_target + target_to_end[1:]

    for i in range(len(start_to_target) - 1):
        assert(start_to_target[i + 1] in graph[start_to_target[i]][1])
    for i in range(len(target_to_end) - 1):
        assert(target_to_end[i + 1] in graph[target_to_end[i]][1])
    assert (path[0] == 0) & (path[-1] == end)
    assert target in path

    return path[1:] 
def dijkstra(start, end):
    visited = set()
    costs = {start: 0}
    parent = {start: None}
    
    while costs:
        current = min((node for node in costs if node not in visited))
        if current is None or current == end:
            break
        visited.add(current)
        node = graph_data.graph_data[global_game_data.current_graph_index][current]
        neighbors = node[1]
        for next_node in neighbors:
            new_cost = costs[current] + 1
            if next_node not in costs or new_cost < costs[next_node]:
                costs[next_node]=new_cost 
                parent[next_node] = current  
    if current == end:
        path = []
        while current is not None:
            path.append(current)
            current = parent[current]
        return path[::-1]
    return None  # return None if no path is found
