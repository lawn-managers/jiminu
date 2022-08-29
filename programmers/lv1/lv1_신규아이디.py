import re

def solution(new_id):
  new_id = new_id.lower()
  new_id = re.sub('[^a-z0-9\.\-\_]', '', new_id)
  new_id = re.sub('\.{2,}', '.', new_id)
  new_id = re.sub('^\.|\.$', '', new_id)
  if len(new_id) == 0 :
    new_id = 'a'
  
  if len(new_id) > 15 :
    new_id = new_id[:15]
    new_id = re.sub('^\.|\.$', '', new_id)
  
  while(len(new_id) <= 2) :
    new_id += new_id[-1]

  print(new_id)
  return new_id


new_id = "abcdefghijklmn.p"	

solution(new_id)