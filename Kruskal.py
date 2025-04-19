class UnionFind:
    def __init__(self, n): self.parent = list(range(n))
    def find(self, x): return x if self.parent[x] == x else self.find(self.parent[x])
    def union(self, x, y): self.parent[self.find(x)] = self.find(y)

def kruskal(graph):
    edges = [(w, u, v) for u in graph for v, w in graph[u]]
    edges.sort()
    uf = UnionFind(len(graph))
    mst = []
    for w, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, w))
    return mst

n = int(input("Enter number of edges: "))
graph = {}
for _ in range(n):
    u, v, cost = input().split()
    cost = int(cost)
    graph.setdefault(u, []).append((v, cost))
    graph.setdefault(v, []).append((u, cost))

print("Kruskal's MST:", kruskal(graph))
