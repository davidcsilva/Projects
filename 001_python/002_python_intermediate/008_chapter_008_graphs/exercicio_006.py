'''
Degree Graph

'''


class GraphDegreeAnalyzer:
    def __init__(self, directed=False):
        self.adj = {}
        self.directed = directed

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)

    def get_degrees(self):
        """
        Returns a dictionary of degree metrics for every vertex:
        - Undirected: {vertex: degree}
        - Directed:   {vertex: {'in': in_deg, 'out': out_deg, 'total': total_deg}}
        """
        if not self.directed:
            return {v: len(neighbors) for v, neighbors in self.adj.items()}

        in_deg = {v: 0 for v in self.adj}
        out_deg = {v: len(neighbors) for v, neighbors in self.adj.items()}

        for u in self.adj:
            for v in self.adj[u]:
                in_deg[v] += 1

        return {
            v: {
                "in": in_deg[v],
                "out": out_deg[v],
                "total": in_deg[v] + out_deg[v],
            }
            for v in self.adj
        }

    def degree_sequence(self):
        """Returns a sorted list (non-increasing) of all vertex degrees."""
        degrees = self.get_degrees()
        if not self.directed:
            return sorted(degrees.values(), reverse=True)
        return sorted((d["total"] for d in degrees.values()), reverse=True)

    def find_hubs(self, top_n=2):
        """Returns the top N vertices with the highest degree."""
        degrees = self.get_degrees()
        if not self.directed:
            return sorted(degrees.items(), key=lambda item: item[1], reverse=True)[:top_n]
        return sorted(
            degrees.items(), key=lambda item: item[1]["total"], reverse=True
        )[:top_n]

    def has_eulerian_circuit(self):
        """
        Checks if a connected graph has an Eulerian Circuit (a closed path
        visiting every edge exactly once) using vertex degrees:
        - Undirected: Every vertex must have an EVEN degree.
        - Directed:   Every vertex must have in_degree == out_degree.
        """
        degrees = self.get_degrees()
        if not self.directed:
            return all(deg % 2 == 0 for deg in degrees.values())
        return all(d["in"] == d["out"] for d in degrees.values())


# --- Example 1: Undirected Network ---
ug = GraphDegreeAnalyzer(directed=False)
ug.add_edge("Hub", "A")
ug.add_edge("Hub", "B")
ug.add_edge("Hub", "C")
ug.add_edge("Hub", "D")
ug.add_edge("A", "B")
ug.add_edge("C", "D")
ug.add_vertex("Isolated")

print("Undirected Degrees: ", ug.get_degrees())
print("Degree Sequence:    ", ug.degree_sequence())
print("Top Hubs:           ", ug.find_hubs(2))
print("Eulerian Circuit?   ", ug.has_eulerian_circuit())

# --- Example 2: Directed Network ---
dg = GraphDegreeAnalyzer(directed=True)
dg.add_edge("API Gateway", "Auth Service")
dg.add_edge("API Gateway", "Order Service")
dg.add_edge("Order Service", "Payment Service")
dg.add_edge("Auth Service", "Payment Service")

print("\nDirected Degrees:")
for node, metrics in dg.get_degrees().items():
    print(f"  {node}: {metrics}")
