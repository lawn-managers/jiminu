from itertools import combinations_with_replacement

N, M = map(int, input().split())
li = [x for x in range(1, N+1)]
       
for i in combinations_with_replacement(li, M) :
    print(' '.join(map(str, i)))