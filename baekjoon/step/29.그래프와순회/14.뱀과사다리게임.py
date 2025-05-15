import sys

board = [[]] + [[[i+(10*j) for i in range(11)]] for j in range(10)]

N, M = map(int, sys.stdin.readline().split())

ladder = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)])
snake = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(M)])

print(board)