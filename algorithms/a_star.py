from utility import reconstruct_path
from graph import graph
from heuristic import heuristic

def a_star(start, goal):
    frontier = [(heuristic(start, goal), 0, start)] #
    explored = set()
    parent = {start: None}
    cost_so_far = {start: 0} # minimum cost found so far to reach each node from the start node
    nodes_expanded = 0

    while frontier: # as long as there are nodes left in the frontier to explore.
        frontier.sort(key=lambda x: x[0]) # sorts the frontier list based on the first element of each tuple, which is f
        f, g, node = frontier.pop(0) # values are unpacked into f, g, and node
        nodes_expanded += 1 
        if node == goal:
            return reconstruct_path(parent, start, goal), nodes_expanded
        if node in explored:
            continue
        explored.add(node)
        for neigh, w in graph[node]:
            new_g = g + w # the cost to reach node + the cost of the edge from node to neigh
            if neigh not in cost_so_far or new_g < cost_so_far[neigh]:
                cost_so_far[neigh] = new_g
                f_val = new_g + heuristic(neigh, goal) #actual cost to reach neigh + estimated cost from neigh to the goal
                frontier.append((f_val, new_g, neigh))
                parent[neigh] = node
    return None, nodes_expanded
