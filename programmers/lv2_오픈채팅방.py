def enter_user(s) :
  return f'{s}님이 들어왔습니다.'

def leave_user(s) :
  return f'{s}님이 나갔습니다.'

def change_user(user_id, s) :
  import re
  s = s.split()
  user_nickname[s[1]] = s[-1]
  
  for pos in user_id[s[1]] :
    change_name = re.sub('([a-zA-z])', '', answer[pos])
    answer[pos] = s[-1] + change_name


answer = []
user_id = {}
user_nickname = {}

def solution(record) :    
  for i in range(len(record)) :
    
    if record[i][0] == 'E' :
      s = record[i].split()
      answer.append(enter_user(s[-1]))
      
      if s[1] in user_id :
        user_id[s[1]].append(len(answer)-1)
        if user_nickname[s[1]] != s[-1] :
          change_user(user_id, record[i])
      else :
        user_id[s[1]] = [len(answer)-1]
      user_nickname[s[1]] = s[-1]
      
    elif record[i][0] == 'L' :
      s = record[i].split()
      answer.append(leave_user(user_nickname[s[-1]]))
      user_id[s[1]].append(len(answer)-1)
      
    elif record[i][0] == 'C' :
      change_user(user_id, record[i])
      
  print(answer)
  return answer




record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution(record)
