N, M = map(int, input().split())

def pow_list(n):
    li = []
    mul = n
    while True :
        if mul > N :
            break
        li.append(mul)
        mul *= n
    return li

def count_num(n, li) :
    n_zero = 0    
    for i in li :
        n_zero += n // i
    return n_zero

five_li = pow_list(5)
two_li = pow_list(2)
    
five = count_num(N, five_li) - (count_num(M, five_li) + count_num(N-M, five_li))
two = count_num(N, two_li) - (count_num(M, two_li) + count_num(N-M, two_li))
print(min(five, two))