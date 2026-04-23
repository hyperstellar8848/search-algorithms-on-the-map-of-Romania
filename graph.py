# Adjacency List (list of tuples)

graph = {
    "Arad": [("Zerind", 75), ("Sibiu", 140), ("Timisoara", 118)],
    "Bucharest": [("Pitesti", 101), ("Fagaras", 211), ("Urziceni", 85), ("Giurgiu", 90)],
    "Craiova": [("Drobeta", 120), ("Rimnicu Vilcea", 146), ("Pitesti", 138)],
    "Drobeta": [("Craiova", 120), ("Mehadia", 75)],
    "Eforie": [("Hirsova", 86)],
    "Fagaras": [("Sibiu", 99), ("Bucharest", 211)],
    "Giurgiu": [("Bucharest", 90)],
    "Hirsova": [("Urziceni", 98), ("Eforie", 86)],
    "Iasi": [("Neamt", 87), ("Vaslui", 92)],
    "Lugoj": [("Timisoara", 111), ("Mehadia", 70)],
    "Mehadia": [("Lugoj", 70), ("Drobeta", 75)],
    "Neamt": [("Iasi", 87)],
    "Oradea": [("Zerind", 71), ("Sibiu", 151)],
    "Pitesti": [("Rimnicu Vilcea", 97), ("Craiova", 138), ("Bucharest", 101)],
    "Rimnicu Vilcea": [("Sibiu", 80), ("Pitesti", 97), ("Craiova", 146)],
    "Sibiu": [("Arad", 140), ("Fagaras", 99), ("Rimnicu Vilcea", 80), ("Oradea", 151)],
    "Timisoara": [("Arad", 118), ("Lugoj", 111)],
    "Urziceni": [("Bucharest", 85), ("Hirsova", 98)],
    "Vaslui": [("Iasi", 92), ("Urziceni", 142)],
    "Zerind": [("Oradea", 71), ("Arad", 75)],
}

for node, neighbours in list(graph.items()):
    for neigh, w in neighbours:
        if node not in [n for n, _ in graph[neigh]]:
            graph[neigh].append((node, w))
