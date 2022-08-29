def solution(N, stages):
    answer_dict = {}
    
    for i in range(1, N+1) :
        fail = len([a for a in stages if a >= i])
        if fail == 0 :
            answer_dict[i] = 0
        else :
            answer_dict[i] = stages.count(i) / fail
    
    # sorted_dict = sorted(answer_dict.items(), key = lambda item : item[1], reverse=True)
    # answer = list(dict(sorted_dict).keys())
    
    answer = sorted(answer_dict, key=lambda k : answer_dict[k], reverse = True)
    return answer