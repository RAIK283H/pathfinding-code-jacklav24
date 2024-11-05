from graph_data import graph_data
import permutation




def main():
    for i in range(0,2):
        print('Graph #', i)
        cycles = permutation.find_h_cycle(graph_data[i])
        if cycles == -1:
            print("No Hamiltonian cycle found.")
        else:
            print("Hamiltonian cycles:", cycles)
            best_cycles = permutation.find_best_cycles(cycles, graph_data[i])
            print('The cycles with the shortest routes by distance are:', best_cycles)
            print()

if __name__ == "__main__":
    main()
