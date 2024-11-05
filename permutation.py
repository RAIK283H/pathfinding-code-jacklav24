import math

def perm(n):
    permutation = list(range(1, n +1))
    direct = [-1] * n
    yield permutation[:]
    while True:
        mobile_index = -1
        mobile_value = -1
        for i in range(n):
            if (direct[i] == -1 and i > 0 and permutation[i] > permutation[i - 1]) or \
               (direct[i] == 1 and i < n - 2 and permutation[i] > permutation[i + 1]):
                if permutation[i] > mobile_value:
                    mobile_index = i
                    mobile_value = permutation[i]
                    
        if mobile_index == -1:
            break
        
        swap_index = mobile_index + direct[mobile_index]
        permutation[mobile_index], permutation[swap_index] = permutation[swap_index], permutation[mobile_index]
        direct[mobile_index], direct[swap_index] = direct[swap_index], direct[mobile_index]
        mobile_index = swap_index

        for i in range(n-1):
            if permutation[i] > mobile_value:
                direct[i] *= -1
        yield permutation[:]

def is_valid_h_cycle(graph, path):
    if (len(path) == 1) or ((len(path) == 2)):
        return True
    for i in range(len(path)-1):
        curr_node = path[i]
        next_node = path[i + 1]
        if next_node not in graph[curr_node][1]:
            return False
    return True

def find_h_cycle(graph):
    n = len(graph) - 1
    h_cycles = []
    
    for permutation in perm(n-1):
        cycle = permutation + [permutation[0]]
        if is_valid_h_cycle(graph, cycle):
            h_cycles.append(cycle[:len(cycle) - 1])
    return h_cycles if h_cycles else -1

def calculate_cycle_dist(graph, cycle):
    total_dist = 0
    for i in range(len(cycle) - 1):
        cord1 = graph[cycle[i]][0]
        cord2 = graph[cycle[i + 1]][0]
        distance = math.sqrt(pow((cord2[0] - cord1[0]),2) + pow((cord2[1] - cord1[1]),2))
        total_dist += distance
    return total_dist

def find_best_cycles(cycles, graph):
    min_distance = float('inf')
    best_cycles = []
    
    for cycle in cycles:
        cycle_dist = calculate_cycle_dist(graph, cycle)
        if cycle_dist < min_distance:
            min_distance = cycle_dist
            best_cycles = [cycle]
        elif cycle_dist == min_distance:
            best_cycles.append(cycle)

    return best_cycles