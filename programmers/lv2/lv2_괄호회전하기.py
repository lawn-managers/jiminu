def move_bracket(s) :
    s = list(s)
    s.append(s[0])
    del s[0]
    s = ''.join(s)
    return s

def check_bracket(s) :
    s = list(s)
    bracket_pair = {')' : '(', '}' : '{', ']' : '['}    
    
    curr_state = []
        
    while(len(s) > 0) :
        check = s[0]
        del s[0]
        
        try :
            if bracket_pair[check] == curr_state[-1] :
                del curr_state[-1]
            else :
                return False
        except :
            curr_state.append(check)
    
    return not(curr_state)

def solution(s):
    answer = 0
    
    for _ in range(len(s)) :
        if check_bracket(s) :
            answer += 1
        s = move_bracket(s)
    
    return answer



s = '[)(]'

print(solution(s))