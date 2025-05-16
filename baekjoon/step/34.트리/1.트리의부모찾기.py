import sys

N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    parent, child = map(int, sys.stdin.readline().split())
    tree[parent].append(child)
    tree[child].append(parent)
    
for i in tree[2:]:
    print(i[0])