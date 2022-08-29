def solution(array, commands):
    answer = []
    
    for com in commands :
        start = com[0]-1
        end = com[1]
        index = com[2]-1
        
        new_array = array[start:end]
        new_array.sort()
        answer.append(new_array[index])
    return answer