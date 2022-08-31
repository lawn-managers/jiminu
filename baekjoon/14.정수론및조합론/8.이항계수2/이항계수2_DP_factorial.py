import sys
sys.setrecursionlimit(100000)

N, K = map(int, input().split())
dic = {}

def memoization(n) :
    if (n == 0 or n == 1) :
        return 1
    
    if n not in dic :
        dic[n] = n * memoization(n-1)
    
    return dic[n]

print(memoization(N) // memoization(K) // memoization(N-K) % 10007)