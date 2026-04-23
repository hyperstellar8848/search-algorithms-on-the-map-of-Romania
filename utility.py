def reconstruct_path(parent, start, goal):
    path = [goal] # working backward from the goal to reconstruct the path
    while path[-1] != start: # path[-1] refers to  the last element in the path list
        path.append(parent[path[-1]])
    path.reverse()
    return path
