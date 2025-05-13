import sys
sys.setrecursionlimit(150000)
N, M, R = map(int, sys.stdin.readline().split())

graph = {i:[] for i in range(1, N+1)}
visited = {i:0 for i in range(1, N+1)}
count = 1

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(R):
    global count
    visited[R] = count
    for x in sorted(graph[R]):
        if not visited[x]:
            count += 1
            graph[R].remove(x)
            graph[x].remove(R)
            dfs(x)
            
# for i in range(1, N + 1):
#     graph[i].sort()

if graph[1]:
    dfs(R)

for key, value in visited.items():
    print(value)