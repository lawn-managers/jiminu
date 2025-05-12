import sys

N, M, R = map(int, sys.stdin.readline().split())

graph = {i:[] for i in range(1, N+1)}
visited = {i:False for i in range(1, N+1)}

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(V, E, R):
    print(R)
    visited[R] = True
    for x in sorted(graph[R]):
        if not visited[x]:
            graph[R].remove(x)
            graph[x].remove(R)
            dfs(V, E, x)
            

dfs(graph, visited, R)

for key, value in visited.items():
    if not value:
        print(0)