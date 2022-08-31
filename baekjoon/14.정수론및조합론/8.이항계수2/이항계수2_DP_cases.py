import sys
sys.setrecursionlimit(100000)

N, K = map(int, input().split())
dic = {}

def memoization(n, k) :
    if (k == 0 or n == k) :
        return 1
    
    if (n,k) not in dic :
        dic[(n,k)] = memoization(n-1, k-1) + memoization(n-1, k)
    
    return dic[(n,k)]

print(memoization(N, K) % 10007)