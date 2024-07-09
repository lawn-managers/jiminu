T = int(input())

for i in range(T):
    nums = list(map(int, input().split()))
    
    answer = 0
    for num in nums:
        answer += num
            
    answer = answer / len(nums)
    print(f'#{i+1} {round(answer)}')