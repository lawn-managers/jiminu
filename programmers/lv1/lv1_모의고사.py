def solution(answers):
    first = [1,2,3,4,5] * 2000
    second = [2,1,2,3,2,4,2,5] * 1250
    third = [3,3,1,1,2,2,4,4,5,5] * 1000
    
    first_answer = 0
    second_answer = 0
    third_answer = 0
    
    for answer, f, s, t in zip(answers, first, second, third) :
        if f == answer :
            first_answer += 1
        if s == answer :
            second_answer += 1
        if t == answer :
            third_answer += 1
    
    dic = {1 : first_answer, 2 : second_answer, 3 : third_answer}
    
    answer = [key for key,value in dic.items() if max(dic.values()) == value]
    
    return answer
  
