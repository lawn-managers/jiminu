from itertools import combinations

N, M = map(int, input().split())
li = [x for x in range(1, N+1)]

for i in combinations(li, M) :
    print(' '.join(map(str, i)))