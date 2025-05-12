import sys
import re
from collections import deque

while True:
    qu = deque()
    passage = sys.stdin.readline().rstrip()
    brackets = re.findall(r'[\[\]\(\)]', passage)
    
    if passage == '.':
        break
    
    for bracket in brackets: 
        if qu and (qu[-1] == '(' and bracket == ')' or qu[-1] == '[' and bracket == ']') :
            qu.pop()
        else :
            qu.append(bracket)

    print('yes') if not qu else print('no')