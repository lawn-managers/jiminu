import math

N, K = map(int, input().split())

cache = [[-1 for _ in range(N+1)] for _ in range(N+1)]

def memoization(n, k) :
    if cache[N][K] != -1 :
        return cache[N][K]
    
    cache[N][K] = memoization(N+1, K) + memoization(N+1, K+1) 
    return cache[N][K]

print(memoization(N,K) % 10007)