import math

N = int(input())
F = math.factorial(N)

result = 0
for i in range(-1, len(str(F))*-1 - 1, -1) :
    if str(F)[i] != '0' :
        print(result)
        break
    result += 1

# t = int(input()) // 5
# print(t + t//5 + t//25)
# 5와 2의 조합이 있으면 0이 하나 생기므로 (10의 소인수분해)