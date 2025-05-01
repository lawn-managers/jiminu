import sys
        
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        
    def pop(self):
        if not self.head:
            return -1
        else:
            data = self.head.data
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.size -= 1
            return data
    def popLeft(self):
        if not self.head:
            return -1
        else:
            data = self.tail.data
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            self.size -= 1
            return data
    def getSize(self):
        return self.size
    def isEmpty(self):
        return self.size == 0   

N = int(sys.stdin.readline())
qu = DoubleLinkedList()

for _ in range(N):
    command = list(sys.stdin.readline().split())
    if command[0] == 'push':
        qu.append(command[1])
    elif command[0] == 'pop':
        if qu.isEmpty():
            print(-1)
        else : print(qu.pop())
    elif command[0] == 'size':
        print(qu.getSize())
    elif command[0] == 'empty':
        print(1) if qu.isEmpty() else print(0)
    elif command[0] == 'front':
        print(qu.head.data) if not qu.isEmpty() else print(-1)
    elif command[0] == 'back':
        print(qu.tail.data) if not qu.isEmpty() else print(-1)