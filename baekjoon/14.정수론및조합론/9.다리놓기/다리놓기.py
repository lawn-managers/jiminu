import math

T = int(input())
for i in range(T) :
    M, N = map(int, input().split())
    print(math.comb(N, M))