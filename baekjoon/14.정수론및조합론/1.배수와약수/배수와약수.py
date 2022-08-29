while True :
    a, b = input().split()
    a = int(a)
    b = int(b)

    if (a == 0 and b == 0) :
        break
    elif (a % b == 0) :
        print('multiple')
    elif (b % a == 0) :
        print('factor')
    else :
        print('neither')