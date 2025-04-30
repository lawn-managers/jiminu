import sys
import queue

qu = queue.Queue()
N = int(sys.stdin.readline())
for _ in range(N):
    command = list(sys.stdin.readline().split())
    if command[0] == 'push':
        qu.put(command[1])
    elif command[0] == 'pop':
        if qu.empty():
            print(-1)
        else : print(qu.get())
    elif command[0] == 'size':
        print(qu.qsize())
    elif command[0] == 'empty':
        print(1) if qu.empty() else print(0)
    elif command[0] == 'front':
        print(qu.queue[0]) if not qu.empty() else print(-1)
    elif command[0] == 'back':
        print(qu.queue[-1]) if not qu.empty() else print(-1)