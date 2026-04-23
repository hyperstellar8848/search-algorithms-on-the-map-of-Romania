This project implements and compares several graph‑search algorithms on the classic Romania road map, an undirected weighted graph that models the distances between 20 Romanian cities.  
The goal is to illustrate how different search algorithms behave in terms of **time**, **nodes expanded**, and **path cost**.

## Usage

* Enter the start city.
* Enter the goal city.
* Choose an algorithm (1–6). <br>
(For DLS you must also provide a depth limit).

Then it prints:

* The discovered path.
* Total travel cost (km).
* Number of nodes expanded.
* A plotted map (via matplotlib).

## Key Takeaways
| Observation | Explanation |
|------------|-------------|
| **A\* is the most efficient optimal algorithm.** | It combines the optimality of UCS with pruning based on the heuristic, reducing the number of expanded nodes. |
| **UCS guarantees optimality but explores more nodes than A\*.** | Without heuristic guidance, UCS must systematically expand the frontier in order of increasing path cost. |
| **BFS / DFS are fast but cannot respect edge weights.** | They treat the graph as unweighted and therefore often return routes that are not cost‑optimal. |
| **DLS can be tuned to reduce expansions.** | When the depth limit matches the depth of the optimal solution, DLS expands fewer nodes than plain DFS or BFS, but it still does not account for edge weights. |
| **Greedy is the fastest but often yields longer paths.** | By following only the heuristic, it is easily attracted to locally promising nodes that may lead to longer overall routes. |
| **The heuristic (squared Euclidean distance) is admissible and consistent.** | For this graph, the heuristic never over‑estimates the true cost, so A\* remains optimal, and Greedy never under‑estimates remaining distance (though it can still choose a sub‑optimal route). |

- Using a heuristic that correlates well with actual distance **dramatically reduces** the search space for **A\*** and **Greedy**.
- **A\*** benefits from the heuristic while still accounting for the accumulated path cost \( g(n) \), which keeps it optimal.
- **Greedy** focuses only on the heuristic value \( h(n) \), so it is even faster in terms of node expansions, but it is **more prone to choosing locally attractive edges that produce longer overall routes**. <br>
Overall, the experiments confirm that **informed search with a well‑designed heuristic** is crucial for efficient route finding on weighted graphs, and **A\*** provides the best balance between optimality and efficiency in this project. 
