T = int(input())

for i in range(T):
    nums = list(map(int, input().split()))
    
    answer = 0
    for num in nums:
        if num % 2 != 0:
            answer += num
            
    print(f'#{i+1} {answer}')