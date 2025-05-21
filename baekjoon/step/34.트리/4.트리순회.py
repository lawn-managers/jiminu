import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def set_left_leaf(self, node):
        self.left = node
    def set_right_leaf(self, node):
        self.right = node

class Tree:
    def __init__(self):
        self.root = None
    
    def set_root(self, node):
        self.root = node
    def get_root(self):
        return self.root

def preorder(node):
    if node is not None:
        print(node.data, end='')
        preorder(node.left)
        preorder(node.right)
    
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end='')
        inorder(node.right)
        
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end='')

N = int(sys.stdin.readline())
nodes = {}
tree = Tree()

for _ in range(N):
    head, left, right = sys.stdin.readline().split()
    if head not in nodes:
        nodes[head] = Node(head)
    node = nodes[head]
    
    if head == 'A':
        tree.set_root(node)
        
    if left != '.':
        if left not in nodes:
            nodes[left] = Node(left)
        node.set_left_leaf(nodes[left])
        
    if right != '.':
        if right not in nodes:
            nodes[right] = Node(right)
        node.set_right_leaf(nodes[right])
        
preorder(tree.get_root())
print()
inorder(tree.get_root())
print()
postorder(tree.get_root())