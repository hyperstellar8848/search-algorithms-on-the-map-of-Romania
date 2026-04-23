from utility import reconstruct_path
from graph import graph

def dls(start, goal, limit):
    frontier = [(start, 0)]      # (node, depth)
    explored = set()
    parent = {start: None}
    nodes_expanded = 0

    while frontier:
        node, depth = frontier.pop()
        nodes_expanded += 1
        if node == goal:
            return reconstruct_path(parent, start, goal), nodes_expanded
        if depth < limit:
            explored.add(node)
            for neigh, _ in graph[node]: # iterate through immediate neighbors of the current node
                if neigh not in explored and all(n != neigh for n, _ in frontier): # not in explored and not in frontier
                    frontier.append((neigh, depth + 1)) #add the newly discovered, valid neighbor to the frontier for future exploration, but only if it’s within the depth limit.
                    parent[neigh] = node
    return None, nodes_expanded
