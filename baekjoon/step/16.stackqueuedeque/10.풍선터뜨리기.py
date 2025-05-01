import sys
from collections import deque

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

queue = deque([i for i in range(1, N+1)])
next_idx = 1

result = ''
while True:
    num = queue.popleft()
    result += f'{num} '
    next_idx = nums[num-1]
    
    if not queue:
        break
    
    if next_idx > 0:
        for _ in range(next_idx - 1):
            queue.append(queue.popleft())
    elif next_idx < 0:
        for _ in range(abs(next_idx)):
            queue.appendleft(queue.pop())
       
print(result)

# import sys

# # N = int(sys.stdin.readline())
# # nums = list(map(int, sys.stdin.readline().split()))
# N = 5
# nums = [3, 2, 1, -3, -1]


# queue = [i for i in range(1, N+1)]
# result = []
# prev_num = 0
# curr_num = 1

# for i in range(N):
#     prev_num = curr_num
    
#     if curr_num >= len(queue):
#         curr_num %= len(queue)
#     elif curr_num < 0:
#         curr_num = len(queue) + curr_num
        
        
#     result.append(str(queue.pop(curr_num-1)))

#     curr_num += prev_num + nums[curr_num-1]

# # print(f'<{str(result)[1:-1]}>')
# print(f'{' '.join(map(str, result))}')