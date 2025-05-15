import sys
from collections import deque
sys.setrecursionlimit(10*6)

N, M, R = map(int, sys.stdin.readline().split())

visited = [0] * (N+1)
graph = [[] for _ in range(N+1)]
count = 1

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(R) :
    global count
    queue = deque([R])
    visited[R] = count
    
    while queue:
        node = queue.popleft()
        for n in sorted(graph[node]):
            if not visited[n]:
                queue.append(n)
                count += 1
                visited[n] = count
                
bfs(R)

for i in visited[1:]:
    print(i)