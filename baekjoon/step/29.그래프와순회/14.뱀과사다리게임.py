import sys
from collections import deque

visited = [0 for _ in range(101)]
ladder = [0 for _ in range(101)]

N, M = map(int, sys.stdin.readline().split())

for _ in range(N+M):
    start, end = map(int, sys.stdin.readline().split())
    ladder[start] = end

# number, count
queue = deque([[1, 0]])
next = 1
while next != 100:
    now, count = queue.popleft()
    
    for i in range(1,7):
        next = now + i
        
        if next == 100:
            print(count+1)
            break
        
        if ladder[next]:
            next = ladder[next]
        
        if not visited[next] or count < visited[next]:
            visited[next] = count + 1
            queue.append([next, count+1])