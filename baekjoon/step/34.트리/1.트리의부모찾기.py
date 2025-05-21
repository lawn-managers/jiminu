import sys
from collections import deque

N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(N-1):
    parent, child = map(int, sys.stdin.readline().split())
    tree[parent].append(child)
    tree[child].append(parent)
    
def bfs(start):
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        
        for n in sorted(tree[node]):
            if not visited[n]:
                visited[n] = node
                queue.append(n)
                
bfs(1)

for i in visited[2:]:
    print(i)