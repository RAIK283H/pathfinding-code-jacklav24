from graph_data import graph_data
import math


def fw(matrix):
    length = len(matrix)
    distance = [[math.inf] * length for _ in range(length)]
    next_node = [[None] * length for _ in range(length)]

    for i in range(length):
        for j in range(length):
            if i == j:
                distance[i][j] = 0
            elif matrix[i][j] != math.inf:
                distance[i][j] = matrix[i][j]
                next_node[i][j] = j 

    for k in range(length):
        for i in range(length):
            for j in range(length):
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    next_node[i][j] = next_node[i][k]

    return distance, next_node


def adj_list_to_matrix(adj_list, num_nodes):
    matrix = [[math.inf] * num_nodes for _ in range(num_nodes)]
    for u, neighbors in enumerate(adj_list):
        for v in neighbors:
            matrix[u][v] = 1
    for i in range(num_nodes):
        matrix[i][i] = 0
    return matrix


def remake_path(next_node, start, end):
    if next_node[start][end] is None:
        return []
    path = [start]
    while start != end:
        start = next_node[start][end]
        path.append(start)
    return path


if __name__ == "__main__":
    graph = graph_data[0]
    num_nodes = len(graph)
    adj_list = [node[1] for node in graph]
    matrix = adj_list_to_matrix(adj_list, num_nodes)
    print('heyo', matrix)
    dist, next_node = fw(matrix)

    print("Distance Matrix:")
    for row in dist:
        print(row)

    print("\nNext Node Matrix:")
    for row in next_node:
        print(row)

    start, end = 0, num_nodes - 1
    path = remake_path(next_node, start, end)
    print(f"\nShortest path from {start} to {end}: {path}")
    print(f"Path length: {dist[start][end]}")