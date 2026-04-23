from utility import reconstruct_path
from graph import graph

def dfs(start, goal):
    frontier = [start]
    explored = set()
    parent = {start: None}
    nodes_expanded = 0

    while frontier:
        node = frontier.pop()  # ***
        nodes_expanded += 1
        if node == goal:
            return reconstruct_path(parent, start, goal), nodes_expanded
        explored.add(node)
        for neigh, _ in graph[node]:
            if neigh not in explored and neigh not in frontier:
                frontier.append(neigh)
                parent[neigh] = node
    return None, nodes_expanded

# bfs removes from front pop(0) FIFO --> queue
# # dfs from back pop()  LIFO --> stack
