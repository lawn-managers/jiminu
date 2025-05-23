import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

def fibonacci(count):
    if n <= 1:
        return
    if count == n:
        return fibo[-1]
    fibo.append(fibo[-1] + fibo[-2])
    fibonacci(count+1)

fibo = [0, 1]

fibonacci(1)
print(fibo[n])

# import sys

# sys.setrecursionlimit(10**6)

# n = int(sys.stdin.readline())

# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(n))