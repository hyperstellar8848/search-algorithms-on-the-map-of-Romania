from coordinates import coords

def heuristic(n, goal):
    # Straight‑line distance used as heuristic.
    lat1, lon1 = coords[n]
    lat2, lon2 = coords[goal]
    return (lat1 - lat2) ** 2 + (lon1 - lon2) ** 2
