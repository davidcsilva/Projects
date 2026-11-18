'''
Directed Graph (Digraph)
'''

from collections import deque


class DirectedGraph:
    def __init__(self):
        self.adj = {}  # Maps vertex -> set of outgoing neighbor vertices

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = set()

    def add_edge(self, u, v):
        """Adds a one-way directed edge from u -> v."""
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].add(v)

    def remove_edge(self, u, v):
        """Removes the directed edge u -> v if it exists."""
        if u in self.adj:
            self.adj[u].discard(v)

    def remove_vertex(self, v):
        """Removes vertex v and all incoming/outgoing edges connected to it."""
        if v not in self.adj:
            return
        del self.adj[v]
        for neighbors in self.adj.values():
            neighbors.discard(v)

    def has_edge(self, u, v):
        return u in self.adj and v in self.adj[u]

    def out_degree(self, v):
        """Number of edges leaving vertex v."""
        if v not in self.adj:
            raise KeyError(f"Vertex '{v}' not found.")
        return len(self.adj[v])

    def in_degree(self, v):
        """Number of edges pointing into vertex v."""
        if v not in self.adj:
            raise KeyError(f"Vertex '{v}' not found.")
        return sum(1 for neighbors in self.adj.values() if v in neighbors)

    def has_cycle(self):
        """
        Detects cycles in a directed graph using 3-state DFS:
        0 = Unvisited, 1 = Visiting (currently on recursion stack), 2 = Visited
        """
        state = {v: 0 for v in self.adj}

        def _dfs(vertex):
            state[vertex] = 1  # Mark as currently visiting
            for neighbor in self.adj[vertex]:
                if state[neighbor] == 1:
                    return True  # Back-edge found -> cycle exists
                if state[neighbor] == 0 and _dfs(neighbor):
                    return True
            state[vertex] = 2  # Mark as completely explored
            return False

        for vertex in self.adj:
            if state[vertex] == 0:
                if _dfs(vertex):
                    return True
        return False

    def topological_sort(self):
        """
        Kahn's Algorithm (BFS): Returns a valid linear ordering of vertices
        for a Directed Acyclic Graph (DAG). Raises ValueError if a cycle exists.
        """
        in_deg = {v: 0 for v in self.adj}
        for u in self.adj:
            for v in self.adj[u]:
                in_deg[v] += 1

        # Start with all vertices that have 0 prerequisites (in-degree == 0)
        queue = deque([v for v, deg in in_deg.items() if deg == 0])
        order = []

        while queue:
            u = queue.popleft()
            order.append(u)
            for v in sorted(self.adj[u]):
                in_deg[v] -= 1
                if in_deg[v] == 0:
                    queue.append(v)

        if len(order) != len(self.adj):
            raise ValueError("Cycle detected: Topological sort is impossible.")

        return order

    def display(self):
        for vertex, neighbors in self.adj.items():
            print(f"{vertex} -> {sorted(neighbors)}")


# --- Example Usage: Course Prerequisites (DAG) ---
dg = DirectedGraph()
dg.add_edge("Intro to CS", "Data Structures")
dg.add_edge("Intro to CS", "Databases")
dg.add_edge("Data Structures", "Algorithms")
dg.add_edge("Databases", "Backend Engineering")
dg.add_edge("Algorithms", "Backend Engineering")

dg.display()
print("\nIn-degree of 'Backend Engineering':",
      dg.in_degree("Backend Engineering"))  # 2
print("Out-degree of 'Intro to CS':       ",
      dg.out_degree("Intro to CS"))         # 2
print("Has cycle?                         ",
      dg.has_cycle())                         # False
print("Study Order (Topological Sort):    ", dg.topological_sort())

# Introducing a circular dependency creates a cycle
dg.add_edge("Algorithms", "Intro to CS")
print("Has cycle after circular edge?     ",
      dg.has_cycle())                         # True
