import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    head, leaf, w = map(int, sys.stdin.readline().split())
    graph[head].append((leaf, w))
    graph[leaf].append((head, w))


def dfs(node, weight):
    for n, w in sorted(graph[node]):
        
        if visited[n] == -1:
            distance = weight + w
            visited[n] = distance
            dfs(n, distance)
            
visited = [-1] * (N+1)
visited[1] = 0
dfs(1, 0)
max_weight = max(visited)
max_node = visited.index(max_weight)

visited = [-1] * (N+1)
visited[max_node] = 0
dfs(max_node, 0)
max_weight = max(visited)

print(max_weight)