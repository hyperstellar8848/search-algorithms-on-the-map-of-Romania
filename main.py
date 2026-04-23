from graph import graph
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.ucs import ucs
from algorithms.dls import dls
from algorithms.a_star import a_star
from algorithms.greedy import greedy
from plotting import plot_path
import time

def main():
    print("Available cities:")
    for city in sorted(graph.keys()):
        print(f"  {city}")
    print()

    start = input("Start city: ").strip()
    goal  = input("Goal city: ").strip()

    if start not in graph or goal not in graph:
        print("Error: city not in graph.")
        return

    print("\nSelect algorithm:")
    print("  1 – BFS")
    print("  2 – DFS")
    print("  3 – UCS")
    print("  4 – DLS")
    print("  5 – A*")
    print("  6 – Greedy")
    algo = input("Choice (1‑6): ").strip()

    start_time = time.time()
    depth_limit = None
    if algo == '4':
        depth_limit = int(input("Depth limit for DLS: ").strip())

    if algo == '1':
        path, nodes = bfs(start, goal)
    elif algo == '2':
        path, nodes = dfs(start, goal)
    elif algo == '3':
        path, nodes = ucs(start, goal)
    elif algo == '4':
        path, nodes = dls(start, goal, depth_limit)
    elif algo == '5':
        path, nodes = a_star(start, goal)
    elif algo == '6':
        path, nodes = greedy(start, goal)
    else:
        print("Invalid choice.")
        return

    elapsed = time.time() - start_time

    if path is None:
        print("No path found.")
        return

    cost = 0
    for i in range(len(path) - 1):
        for neigh, w in graph[path[i]]:
            if neigh == path[i + 1]:
                cost += w
                break

    print(f"\nPath: {' -> '.join(path)}")
    print(f"Cost: {cost}")
    print(f"Nodes expanded: {nodes}")
    print(f"Time passed: {elapsed:.4f} seconds")

    plot_path(path)

if __name__ == "__main__":
    main()
