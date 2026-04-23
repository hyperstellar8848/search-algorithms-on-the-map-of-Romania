from utility import reconstruct_path
from graph import graph

def bfs(start, goal):
    frontier = [start] # nodes that've been discovered but whose neighbors haven't
    explored = set() # visited nodes that had their neighbors processed
    parent = {start: None} #crucial for reconstructing the path. stores every nodes' predecessor
    nodes_expanded = 0  # used as a metric for the search’s efficiency. (counter)

    while frontier:
        node = frontier.pop(0)
        nodes_expanded += 1
        if node == goal:
            return reconstruct_path(parent, start, goal), nodes_expanded
        # if we didnt't reach goal yet:
        explored.add(node) # marking it -as explored- prevents infinite loops
        for neigh, _ in graph[node]: #iterates through neighbors of the current node, ignores w
            if neigh not in explored and neigh not in frontier: # = this is a new, unvisited node
                frontier.append(neigh)
                parent[neigh] = node
    return None, nodes_expanded # frontier is empty but the goal was never found-> return none
