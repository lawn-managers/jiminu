from itertools import product

N, M = map(int, input().split())
li = [x for x in range(1, N+1)]

for i in product(li, repeat=M) :
    print(' '.join(map(str, i)))