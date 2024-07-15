def check_view(i, curr):
    if (aparts_height[i-2] < curr and
        aparts_height[i-1] < curr and
        aparts_height[i+1] < curr and 
        aparts_height[i+2] < curr):
        return True
    return False


for i in range(1, 11):
    T = int(input())

    aparts_height = list(map(int, input().split()))

    answer = 0

    for apart_queue in range(2, len(aparts_height)-2):
        apart_height = aparts_height[apart_queue]
        
        for curr_floor in range(apart_height, 0, -1):
            if check_view(apart_queue, curr_floor):
                answer += 1
            else:
                break
            
    print(f'#{i} {answer}')

