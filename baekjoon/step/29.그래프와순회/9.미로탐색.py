import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

labyrinth = [[]] + [[0] + [int(i) for i in sys.stdin.readline().rstrip()] for _ in range(N)] + [[0] * (M+1)]
visited = [[0 for _ in range(M+1)] for _ in range(N+1)]
graph = [[[] for _ in range(M+1)] for _ in range(N+1)]

queue = deque([
    [[1,1], 1]
])

for i in range(1, M+1):
    for j in range(1, N+1):
        if not labyrinth[j][i]:
            continue
        
        if j < N and labyrinth[j+1][i]: # down
            graph[j+1][i].append([j,i])
            graph[j][i].append([j+1,i])
        if i < M and labyrinth[j][i+1]: # right
            graph[j][i+1].append([j,i])
            graph[j][i].append([j,i+1])
            
def bfs(start):
    visited[1][1] = 1
    while start:
        node = start.popleft()
        x, y, count = node[0][0], node[0][1], node[1]
        
        if x == N and y == M:
            print(count)
            break
        
        for n in sorted(graph[x][y]):
            if not visited[n[0]][n[1]]:
                start.append([n, count+1])
                visited[n[0]][n[1]] = 1
bfs(queue)