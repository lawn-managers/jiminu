import sys
from collections import deque

qu = deque()
N = int(sys.stdin.readline())
for _ in range(N):
    command = list(sys.stdin.readline().split())
    if command[0] == 'push':
        qu.append(command[1])
    elif command[0] == 'pop':
        if not qu:
            print(-1)
        else : print(qu.popleft())
    elif command[0] == 'size':
        print(len(qu))
    elif command[0] == 'empty':
        print(1) if not qu else print(0)
    elif command[0] == 'front':
        print(qu[0]) if qu else print(-1)
    elif command[0] == 'back':
        print(qu[-1]) if qu else print(-1)