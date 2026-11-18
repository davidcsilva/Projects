'''
Undirected Graph
'''

from collections import deque


class UndirectedGraph:
    def __init__(self):
        self.adj = {}  # Maps vertex -> set of connected neighbor vertices

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = set()

    def add_edge(self, u, v):
        """Adds an undirected (two-way) edge between u and v."""
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].add(v)
        self.adj[v].add(u)

    def remove_edge(self, u, v):
        """Removes the two-way edge between u and v if it exists."""
        if u in self.adj and v in self.adj[u]:
            self.adj[u].remove(v)
            self.adj[v].remove(u)

    def remove_vertex(self, v):
        """Removes vertex v and cleans up all incident edges."""
        if v not in self.adj:
            return
        for neighbor in list(self.adj[v]):
            self.adj[neighbor].remove(v)
        del self.adj[v]

    def has_edge(self, u, v):
        return u in self.adj and v in self.adj[u]

    def degree(self, v):
        """Returns the number of edges connected to vertex v."""
        if v not in self.adj:
            raise KeyError(f"Vertex '{v}' not found.")
        return len(self.adj[v])

    def shortest_path(self, start, goal):
        """Finds the shortest unweighted path between start and goal using BFS."""
        if start not in self.adj or goal not in self.adj:
            return None
        if start == goal:
            return [start]

        visited = {start}
        queue = deque([(start, [start])])

        while queue:
            current, path = queue.popleft()
            for neighbor in sorted(self.adj[current]):
                if neighbor == goal:
                    return path + [neighbor]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return None  # No path exists (disconnected components)

    def has_cycle(self):
        """Detects whether the undirected graph contains at least one cycle using DFS."""
        visited = set()

        def _dfs(vertex, parent):
            visited.add(vertex)
            for neighbor in self.adj[vertex]:
                if neighbor not in visited:
                    if _dfs(neighbor, vertex):
                        return True
                # If neighbor is already visited and is NOT the immediate parent, a cycle exists
                elif neighbor != parent:
                    return True
            return False

        for vertex in self.adj:
            if vertex not in visited:
                if _dfs(vertex, parent=None):
                    return True
        return False

    def display(self):
        for vertex, neighbors in self.adj.items():
            print(f"{vertex} -- {sorted(neighbors)}")


# --- Example Usage ---
g = UndirectedGraph()
g.add_edge("Alice", "Bob")
g.add_edge("Alice", "Charlie")
g.add_edge("Bob", "David")
g.add_edge("Charlie", "David")
g.add_edge("David", "Eve")

g.display()
print("\nDegree of David:", g.degree("David"))                         # 3
# True (Alice-Bob-David-Charlie)
print("Has cycle?     ", g.has_cycle())
print("Shortest path: ", g.shortest_path("Alice", "Eve")
      )             # ['Alice', 'Bob', 'David', 'Eve']

g.remove_edge("Charlie", "David")
print("Cycle after removing Charlie-David:", g.has_cycle())           # False
