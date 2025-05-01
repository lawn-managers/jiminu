import sys

N, K = map(int, sys.stdin.readline().split())

circle = [i for i in range(1, N+1)]
result = []
curr_num = 0

for i in range(N):
    curr_num += (K-1)
    if curr_num >= len(circle) and circle:
        curr_num %= len(circle)
    result.append(str(circle.pop(curr_num)))

# print(f'<{str(result)[1:-1]}>')
print(f'<{', '.join(map(str, result))}>')