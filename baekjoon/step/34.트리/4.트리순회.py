import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def set_left_leaf(self, node):
        self.left = node
    def set_left_right(self, node):
        self.right = node

class Tree:
    def __init__(self, data):
        self.root = data


N = int(sys.stdin.readline())

for _ in range(N):
    head, left, right = sys.stdin.readline().split()
    
    