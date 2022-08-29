import re

def solution(s): 
    alpha = ['zero', 'one', 'two', 'three', 'four', 'five',
         'six', 'seven', 'eight', 'nine']
    num = [0,1,2,3,4,5,6,7,8,9]
    
    for i in range(len(alpha)) :
        s = re.sub(alpha[i], str(num[i]), s)
    answer = int(s)
    return answer