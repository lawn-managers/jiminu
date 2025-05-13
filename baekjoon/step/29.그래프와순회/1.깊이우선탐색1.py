import sys
sys.setrecursionlimit(150000)
N, M, R = map(int, sys.stdin.readline().split())

# WARNING: [[]] * (N+1) will be copy themselves. then every array is the same.
# NOTE: list
# graph = [[]] * (N+1)
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

# NOTE: dictionary
# graph = {i:[] for i in range(1, N+1)}
# visited = {i:0 for i in range(1, N+1)}

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
            dfs(x)
            
dfs(R)

if isinstance(visited, list): 
    for i in visited[1:]:
        print(i)
else:
    for k, v in visited.items():
        print(v)