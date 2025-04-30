import sys
from collections import deque

qu = deque()
N = int(sys.stdin.readline())
for _ in range(N):
    command = list(map(int, sys.stdin.readline().split()))
    if command[0] == 1:
        qu.appendleft(command[1])
    elif command[0] == 2:
        qu.append(command[1])
    elif command[0] == 3:
        print(qu.popleft()) if qu else print(-1)
    elif command[0] == 4:
        print(qu.pop()) if qu else print(-1)
    elif command[0] == 5:
        print(len(qu))
    elif command[0] == 6:
        print(1) if not qu else print(0)
    elif command[0] == 7:
        print(qu[0]) if qu else print(-1)
    elif command[0] == 8:
        print(qu[-1]) if qu else print(-1)