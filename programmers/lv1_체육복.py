
lost = [4,2]
reserve  = [3,5]
n = 5

def solution(n, lost, reserve):
    state = True
    lost.sort()
    reserve.sort()
    
    while(len(lost) > 0 and len(reserve) > 0 and state) :
        lost, reserve, state = same_element_delete(lost, reserve)
    
    state = True
    while(len(lost) > 0 and len(reserve) > 0 and state) :
        lost, reserve, state = calc(lost, reserve) 
                
    answer = n - len(lost)
    print(answer)
    return answer

def calc(lost, reserve) :
    for lo in lost :
        for re in reserve :
            if re - 1 == lo or re + 1 == lo :
                reserve.remove(re)
                lost.remove(lo)
                return lost, reserve, True
            
    return lost, reserve, False

def same_element_delete(lost, reserve) :
    for lo in lost :
        if lo in reserve :
            lost.remove(lo)
            reserve.remove(lo)
            return lost, reserve, True
        
    return lost, reserve, False
    
    
    
solution(n, lost, reserve)