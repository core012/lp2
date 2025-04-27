class UnionFind:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}  # parent dictionary for string nodes

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

def kruskal(graph):
    edges = [(w, u, v) for u in graph for v, w in graph[u]]
    edges.sort()
    uf = UnionFind(graph.keys())
    mst = []
    for w, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, w))
    return mst
    
n = int(input("Enter number of edges: "))
graph = {}

for _ in range(n):
    u, v, cost = input("Enter edge (u v cost): ").split()
    cost = int(cost)
    graph.setdefault(u, []).append((v, cost))
    graph.setdefault(v, []).append((u, cost))

mst = kruskal(graph)

print("Kruskal's MST:")
for u, v, w in mst:
    print(f"{u} - {v}: {w}")
