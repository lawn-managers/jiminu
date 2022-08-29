from itertools import permutations

def split_exp(s) :
    answer = []
    param = ''
    for i in range(len(s)) :
        if s[i].isdigit() :
            param += s[i]
        else :
            answer.append(param)
            answer.append(s[i])
            param = ''
    answer.append(param)
    return answer
        
def solution(expression):
    answer= []

    for oper in permutations(['+','-','*']) :
        exp = split_exp(expression)
        for op in oper :
            while (op in exp) :
                index = exp.index(op)
                ex = exp[index-1] + op + exp[index+1]
                for _ in range(3) :
                    del exp[index-1]
                
                exp.insert(index-1, str(eval(ex)))
        answer.append(abs(int(exp[0])))
    
    return max(answer)

# 실패
# import re
# def merge_minus(s) :
#     calc = f'-{2,}'
#     p = re.search(calc, s)
#     if (p) :
#         minus_group = p.group()
#         if len(minus_group) % 2 == 1 :
#             return s.replace(calc, '-')
#         return s.replace(calc, '+')
    
#     return s
    
# def solution(expression):
#     answer= []
#     operator = list(permutations(['+','-','*']))
#     # operator = [['*','-','+']]

#     for oper in operator :
#         exp = expression
#         for i in range(len(oper)) :
#             calc = f'\d+\{oper[i]}-*\d+'
#             p = re.search(calc, exp)
            
#             while p :
#                 start = p.span()[0]
#                 end = p.span()[1]
#                 if start == 1 :
#                     calc_exp = '-' + p.group()
#                 else :    
#                     calc_exp = p.group()
#                 result = eval(calc_exp)
                
#                 # exp = exp[:start] + str(result) + exp[end:]
#                 # # exp = re.sub(calc, str(result), exp)
#                 exp = exp.replace(calc_exp, str(result))
#                 exp = merge_minus(exp)
#                 p = re.search(calc, exp)

#         answer.append(abs(int(eval(exp))))
            
#     return max(answer)