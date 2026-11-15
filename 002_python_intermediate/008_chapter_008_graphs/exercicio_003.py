'''
Weighted Graph
'''

import heapq


class WeightedGraph:
    def __init__(self, directed=False):
        self.adj = {}  # Maps vertex -> {neighbor: weight}
        self.directed = directed

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = {}

    def add_edge(self, u, v, weight):
        """Adds an edge between u and v with a numerical weight."""
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u][v] = weight
        if not self.directed:
            self.adj[v][u] = weight

    def get_weight(self, u, v):
        """Returns the weight of edge (u, v), or None if no edge exists."""
        return self.adj.get(u, {}).get(v)

    def dijkstra(self, start, goal):
        """
        Finds the lowest-cost path from 'start' to 'goal' for non-negative weights.
        Returns (total_cost, path_list).
        """
        if start not in self.adj or goal not in self.adj:
            return float("inf"), []

        # Min-Heap storing (accumulated_cost, current_vertex)
        pq = [(0, start)]
        distances = {v: float("inf") for v in self.adj}
        distances[start] = 0
        previous = {v: None for v in self.adj}

        while pq:
            current_cost, u = heapq.heappop(pq)

            # Skip stale heap entries
            if current_cost > distances[u]:
                continue

            if u == goal:
                break

            for neighbor, weight in self.adj[u].items():
                if weight < 0:
                    raise ValueError(
                        "Dijkstra's algorithm does not support negative weights.")
                new_cost = current_cost + weight
                if new_cost < distances[neighbor]:
                    distances[neighbor] = new_cost
                    previous[neighbor] = u
                    heapq.heappush(pq, (new_cost, neighbor))

        if distances[goal] == float("inf"):
            return float("inf"), []

        # Reconstruct path backwards from goal to start
        path = []
        curr = goal
        while curr is not None:
            path.append(curr)
            curr = previous[curr]
        path.reverse()

        return distances[goal], path

    def display(self):
        for vertex, edges in self.adj.items():
            formatted = ", ".join(
                f"{nbr} (cost: {w})" for nbr, w in edges.items())
            print(f"{vertex} -> {formatted}")


# --- Example Usage: City Road Network ---
roads = WeightedGraph(directed=False)
roads.add_edge("São Paulo", "Campinas", 95)
roads.add_edge("São Paulo", "São José dos Campos", 90)
roads.add_edge("Campinas", "Ribeirão Preto", 220)
roads.add_edge("Campinas", "Sorocaba", 85)
roads.add_edge("Sorocaba", "São Paulo", 100)
roads.add_edge("São José dos Campos", "Ribeirão Preto", 310)

roads.display()

cost, route = roads.dijkstra("Sorocaba", "Ribeirão Preto")
print(f"\nShortest route: {' -> '.join(route)} ({cost} km)")
