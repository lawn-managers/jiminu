from math import gcd

num = int(input())
n_list = list(map(int, input().split()))

for n in n_list[1:] :
    gcd_num = gcd(n_list[0], n)
    print(str(n_list[0]//gcd_num) + '/' + str(n//gcd_num))