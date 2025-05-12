import sys
from collections import deque

brackets = ['(',
            ')',
            '[',
            ']' ]

while True: 
    qu = deque()
    word = sys.stdin.readline().rstrip()
    
    if word == '.':
        break
    for w in word:
        if qu and ( qu[-1] == '(' and w == ')' or qu[-1] == '[' and w == ']') :
            qu.pop()
        elif w in brackets :
            qu.append(w)
        
    print('yes') if not qu else print('no')