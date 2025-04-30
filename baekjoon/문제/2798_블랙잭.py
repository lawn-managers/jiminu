import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

candidates = list(combinations(cards, 3))
result = 0

for card in candidates:
    if result < sum(card) <= M:
        result = sum(card)
print(result)