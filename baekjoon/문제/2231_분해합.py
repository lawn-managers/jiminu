import sys

N = int(sys.stdin.readline())

for num in range(N):
    result = num
    
    for n in str(num):
        result += int(n)
    
    if result == N:
        print(num)
        break
else:
    print(0)