T = int(input())
for test_case in range(1, T + 1):
    
    max_num = 0
    test_list = list(map(int, input().split()))
    for i in test_list :
        if max_num < i :
            max_num = i
    print('#%d %d'%(test_case, max_num))