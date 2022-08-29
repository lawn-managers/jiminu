from itertools import combinations

def find_prime_num(number) :
    for i in range(2, number) :
        if number % i == 0 :
            return 0
    return 1
    
def solution(nums):
    answer = 0
    
    com = list(combinations(nums, 3))
    
    for li in com :
        number = li[0] + li[1] + li[2]
        prime_number = find_prime_num(number)
        answer += prime_number
        
    return answer