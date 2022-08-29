def solution(s) :
  answer = []
  
  for i in range(len(s)) :
    try :
      if answer[-1] == s[i] :
        answer.pop()
      else :
        answer.append(s[i])
    except :
      answer.append(s[i])
  if len(answer) == 0 :
    return 1
  else :
    return 0

# 기능은 동일하나 2배 느림
# def solution(s) :
#   import re
#   regex = '[a]{2}|[b]{2}|[c]{2}|[d]{2}|[e]{2}|[f]{2}|[g]{2}|[h]{2}|[i]{2}|[j]{2}|[k]{2}|[l]{2}|[m]{2}|[n]{2}|[o]{2}|[p]{2}|[q]{2}|[r]{2}|[s]{2}|[t]{2}|[u]{2}|[v]{2}|[w]{2}|[x]{2}|[y]{2}|[z]{2}|'
#   while True :
    
#     s1 = re.sub(regex, '', s)
#     if s1 != s :
#       s = s1
#     else :  
#       if len(s) == 0 :
#         return 1
#       else :
#         return 0