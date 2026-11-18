'''
Acyclic Graph
'''

from collections import deque


class DirectedAcyclicGraph:
    def __init__(self):
        self.adj = {}  # Maps vertex -> {neighbor: weight}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = {}

    def add_edge(self, u, v, weight=1):
        """
        Adds a directed edge u -> v only if it does NOT create a cycle.
        Raises ValueError if the edge would introduce a cycle.
        """
        self.add_vertex(u)
        self.add_vertex(v)

        if u == v or self._can_reach(start=v, target=u):
            raise ValueError(f"Adding edge '{u} -> {v}' would create a cycle.")

        self.adj[u][v] = weight

    def _can_reach(self, start, target):
        """Checks via BFS if 'target' is already reachable from 'start'."""
        visited = {start}
        queue = deque([start])

        while queue:
            curr = queue.popleft()
            if curr == target:
                return True
            for neighbor in self.adj[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return False

    def topological_sort(self):
        """Returns vertices in topological order using Kahn's Algorithm."""
        in_degree = {v: 0 for v in self.adj}
        for u in self.adj:
            for v in self.adj[u]:
                in_degree[v] += 1

        queue = deque([v for v, deg in in_degree.items() if deg == 0])
        order = []

        while queue:
            u = queue.popleft()
            order.append(u)
            for v in self.adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        return order

    def longest_path(self, start):
        """
        Computes the longest path (Critical Path) from 'start' to all other
        reachable vertices in O(V + E) time—something NP-hard on general cyclic graphs.
        """
        topo_order = self.topological_sort()
        dist = {v: float("-inf") for v in self.adj}
        dist[start] = 0

        for u in topo_order:
            if dist[u] != float("-inf"):
                for v, weight in self.adj[u].items():
                    if dist[u] + weight > dist[v]:
                        dist[v] = dist[u] + weight

        return dist


# --- Example Usage: Build / CI-CD Pipeline (DAG) ---
pipeline = DirectedAcyclicGraph()

# Edges represent task dependencies with execution duration (in minutes)
pipeline.add_edge("Checkout Code", "Install Deps", weight=2)
pipeline.add_edge("Install Deps", "Run Unit Tests", weight=5)
pipeline.add_edge("Install Deps", "Build Assets", weight=3)
pipeline.add_edge("Run Unit Tests", "Deploy Staging", weight=4)
pipeline.add_edge("Build Assets", "Deploy Staging", weight=4)

print("Execution Order:", pipeline.topological_sort())
print("Critical Path Durations from 'Checkout Code':")
for step, duration in pipeline.longest_path("Checkout Code").items():
    print(f"  {step}: {duration} min")

# Attempting to add a cyclic dependency is automatically blocked
try:
    pipeline.add_edge("Deploy Staging", "Checkout Code")
except ValueError as err:
    print("\nCycle Guard Triggered:", err)
