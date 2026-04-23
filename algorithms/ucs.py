from utility import reconstruct_path
from graph import graph

def ucs(start, goal):
    frontier = [(0, start)]    # (cost, node)
    explored = set()
    parent = {start: None}
    cost_so_far = {start: 0}
    nodes_expanded = 0

    while frontier:
        frontier.sort(key=lambda x: x[0])  # priority queue. lowest cost comes first
        cost, node = frontier.pop(0)  # removes and returns
        nodes_expanded += 1
        if node == goal:
            return reconstruct_path(parent, start, goal), nodes_expanded
        if node in explored:
            continue
        explored.add(node)
        for neigh, w in graph[node]:
            new_cost = cost + w  # cost of the path so far + w = new cost
            if neigh not in cost_so_far or new_cost < cost_so_far[neigh]:
                cost_so_far[neigh] = new_cost
                frontier.append((new_cost, neigh))
                parent[neigh] = node
    return None, nodes_expanded
