from itertools import permutations

N, M = map(int, input().split())
li = [x for x in range(1, N+1)]

for i in permutations(li, M) :
    print(' '.join(map(str, i)))