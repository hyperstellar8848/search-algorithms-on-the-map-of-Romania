import matplotlib.pyplot as plt  
from coordinates import coords
from graph import graph


def plot_path(path):
    # coordinates of all nodes
    all_lats = [c[0] for c in coords.values()]
    all_lons = [c[1] for c in coords.values()]

    plt.figure(figsize=(10, 8))
    plt.scatter(all_lons, all_lats, color='lightgray', s=50, zorder=1)

    # all edges
    for node, neighbours in graph.items():
        for neigh, _ in neighbours:
            plt.plot([coords[node][1], coords[neigh][1]],
                     [coords[node][0], coords[neigh][0]],
                     color='gray', linewidth=0.8, zorder=0)

    # path
    path_lats = [coords[n][0] for n in path]
    path_lons = [coords[n][1] for n in path]
    plt.plot(path_lons, path_lats, color='red', linewidth=2, zorder=2, label='Path')
    plt.scatter(path_lons, path_lats, color='red', s=70, zorder=3)

    plt.title('Romania Road Network – Found Path')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend()
    plt.grid(True)
    plt.show()
