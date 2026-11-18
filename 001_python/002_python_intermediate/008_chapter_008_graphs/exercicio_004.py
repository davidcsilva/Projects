'''
Cyclic Graph
'''


class CyclicGraph:
    def __init__(self, directed=True):
        self.adj = {}
        self.directed = directed

    def add_edge(self, u, v):
        self.adj.setdefault(u, [])
        self.adj.setdefault(v, [])
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)

    def find_cycle(self):
        """
        Detects a cycle and returns the list of vertices forming it,
        or None if the graph is acyclic.
        """
        if self.directed:
            return self._find_directed_cycle()
        return self._find_undirected_cycle()

    def _find_directed_cycle(self):
        # 0 = Unvisited, 1 = Visiting (in current DFS path), 2 = Completely visited
        state = {v: 0 for v in self.adj}
        parent = {}

        def dfs(u):
            state[u] = 1
            for v in self.adj[u]:
                if state[v] == 1:
                    # Back-edge u -> v found; reconstruct cycle from v to u
                    cycle = [v, u]
                    curr = u
                    while curr != v:
                        curr = parent[curr]
                        cycle.append(curr)
                    cycle.reverse()
                    return cycle
                if state[v] == 0:
                    parent[v] = u
                    res = dfs(v)
                    if res:
                        return res
            state[u] = 2
            return None

        for vertex in self.adj:
            if state[vertex] == 0:
                cycle = dfs(vertex)
                if cycle:
                    return cycle
        return None

    def _find_undirected_cycle(self):
        visited = set()
        parent = {}

        def dfs(u, par):
            visited.add(u)
            for v in self.adj[u]:
                if v == par:
                    continue  # Ignore the immediate edge we just came from
                if v in visited:
                    # Cycle found; reconstruct path from v to u
                    cycle = [v, u]
                    curr = u
                    while curr != v:
                        curr = parent[curr]
                        cycle.append(curr)
                    cycle.reverse()
                    return cycle
                parent[v] = u
                res = dfs(v, u)
                if res:
                    return res
            return None

        for vertex in self.adj:
            if vertex not in visited:
                cycle = dfs(vertex, par=None)
                if cycle:
                    return cycle
        return None


# --- Example 1: Directed Cyclic Graph (Deadlock / Circular Dependency) ---
dg = CyclicGraph(directed=True)
dg.add_edge("Service A", "Service B")
dg.add_edge("Service B", "Service C")
dg.add_edge("Service C", "Service A")  # Creates cycle A -> B -> C -> A
dg.add_edge("Service C", "Service D")

print("Directed cycle found:  ", dg.find_cycle())

# --- Example 2: Undirected Cyclic Graph (Closed Network Loop) ---
ug = CyclicGraph(directed=False)
ug.add_edge("Router 1", "Router 2")
ug.add_edge("Router 2", "Router 3")
ug.add_edge("Router 3", "Router 4")
# Creates cycle Router 2 - Router 3 - Router 4 - Router 2
ug.add_edge("Router 4", "Router 2")

print("Undirected cycle found:", ug.find_cycle())
