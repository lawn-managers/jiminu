num = int(input())
n_list = list(map(int, input().split()))

if (num < 2) :
    print(min(n_list)**2)
else :
    print(min(n_list) * max(n_list))