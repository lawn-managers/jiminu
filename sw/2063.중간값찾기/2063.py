T = int(input())

nums = list(map(int, input().split()))

nums.sort()

print(f'{nums[int(T/2)]}')
