def solution(dartResult):
    answer = 0
    str = ''
    result = []
    number = []
    alpha = []
    sang = []
    
    calc = {'S' : 1, 'D' : 2, 'T' : 3}
    
    for i in dartResult :
        if i.isdigit() :
            str += i
        elif i.isalpha() :
            number.append(str)
            alpha.append(i)
            str = ''
        else :
            sang.append([len(number)-1, i])
            
    for i in range(3) :
        num = number[i]
        alp = calc[alpha[i]]
        result.append([f'{num} ** {alp}'])
    
    for i in sang :
        if i[1] == '#' :
            result[i[0]] += '* -1'
        elif i[1] == '*' :
            result[i[0]] += '* 2'
            if i[0] != 0 :
                result[i[0]-1] += '* 2'
    
    for i in result :
        i = ''.join(i)
        answer += eval(i)
        
    print(result)
    print(answer)
      
    return answer
  
dartResult = '1D2S#10S'
solution(dartResult)