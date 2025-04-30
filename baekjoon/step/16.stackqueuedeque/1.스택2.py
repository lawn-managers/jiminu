class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.stack:
            return -1
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def empty(self):
        return 1 if not self.stack else 0

    def top(self):
        if not self.stack:
            return -1
        return self.stack[-1]
    
    def enter(self, num):
        if num[0] == 1:
            self.push(num[1])
        elif num[0] == 2:
            print(self.pop())
        elif num[0] == 3:
            print(self.size())
        elif num[0] == 4:
            print(self.empty())
        elif num[0] == 5:
            print(self.top())

import sys

N = int(sys.stdin.readline())
stack = Stack()

for _ in range(N):
    num = list(map(int, sys.stdin.readline().split()))
    stack.enter(num)