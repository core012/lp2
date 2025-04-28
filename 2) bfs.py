from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # def bfs(self, start):
    #     visited = set()
    #     queue = deque([start])
    #     visited.add(start)
    #     while queue:
    #         v = queue.popleft()
    #         print(v, end='-> 'if queue else' ')
    #         for neighbor in self.graph[v]:
    #             if neighbor not in visited:
    #                 visited.add(neighbor)
    #                 queue.append(neighbor)

    def bfs(self, queue, visited, is_first=True):
        if not queue:
            return

        vertex = queue.popleft()
        if is_first:
            print(vertex, end='')
        else:
            print(f"-> {vertex}", end='')

        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

        self.bfs(queue, visited, False)


# Input
g = Graph()
n = int(input("Enter number of edges: "))
print("Enter edges (u v):")
for _ in range(n):
    u, v = map(int, input().split())
    g.add_edge(u, v)

start = int(input("Enter starting node: "))
print("BFS traversal:")
visited = set([start])
queue = deque([start])
g.bfs(queue, visited)
# g.bfs(start)
print()
