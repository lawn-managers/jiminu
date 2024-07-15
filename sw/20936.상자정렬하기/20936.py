def equal_index_and_value(num_list, i):
    if num_list[i-1] == i:
        return True
    return False

def organize_list(num_list, curr_num):
    num_list.append(len(num_list)+1)
    next_index = len(num_list) - 1
    moving_index = ''
    count = 0
    while(not(equal_index_and_value(num_list, curr_num))):
        curr_index = num_list.index(curr_num) + 1
        moving_index += f'{curr_index} '
        num_list[curr_index-1], num_list[next_index] = num_list[next_index], num_list[curr_index-1]
        
        next_index = curr_index - 1
        curr_num = curr_index
        count += 1
        
    num_list.pop()
    return num_list, count, moving_index
    

T = int(input())

for i in range(T):
    highest_number = int(input())
    num_list = list(map(int, input().split()))
    answer = ''
    count = 0
    
    for curr_num in range(highest_number, 1, -1):
        curr_index = num_list.index(curr_num) + 1
        if equal_index_and_value(num_list, curr_num):
            continue
        
        num_list, moving_count, moving_index = organize_list(num_list, curr_num)
        answer += moving_index
        count += moving_count
    print(count)
    print(answer)