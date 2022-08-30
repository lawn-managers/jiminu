from math import gcd

num = int(input())
n_list = []
sub_list = []

for i in range(num) :
    n_list.append(int(input()))

gcd_num = abs(n_list[0] - n_list[1])
for n in range(1, len(n_list)-1) :
    gcd_num = gcd(gcd_num, abs(n_list[n] - n_list[n+1]))

result = set()
for i in range(2, int(gcd_num**0.5)+1) :
    if (gcd_num % i == 0) :
        result.add(i)
        result.add(gcd_num // i)
result.add(gcd_num)
    
r = ''
for n in sorted(result) :
    r += str(n) + ' '
print(r)