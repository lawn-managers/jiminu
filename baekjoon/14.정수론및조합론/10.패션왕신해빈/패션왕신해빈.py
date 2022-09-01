T = int(input())
for i in range(T) :
    result = 1
    dic = {}
    C = int(input()) 
    
    for j in range(C) :
        clothes = input().split()
        if (clothes[1] not in dic) :
            dic[clothes[1]] = 1
            continue
        dic[clothes[1]] += 1
    
    for j in dic.values() :
        result *= (j + 1)

    print(result - 1)