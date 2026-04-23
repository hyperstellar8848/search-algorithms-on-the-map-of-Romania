from utility import reconstruct_path
from graph import graph
from heuristic import heuristic

def greedy(start, goal):
    frontier = [(heuristic(start, goal), start)]   # (h, node)
    explored = set()
    parent = {start: None}
    nodes_expanded = 0

    while frontier:
        frontier.sort(key=lambda x: x[0]) # the node with the lowest h is always considered next.          
        h, node = frontier.pop(0)
        nodes_expanded += 1
        if node == goal:
            return reconstruct_path(parent, start, goal), nodes_expanded
        if node in explored:
            continue
        explored.add(node)
        for neigh, _ in graph[node]:
            if neigh not in explored and all(n != neigh for _, n in frontier):
                frontier.append((heuristic(neigh, goal), neigh))
                parent[neigh] = node
    return None, nodes_expanded
