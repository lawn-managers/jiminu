from itertools import permutations

def solution(k, dungeons):
    answer = []
    
    d_list = list(permutations(dungeons, len(dungeons)))
    for dungeon in d_list :
        tatigue = k
        state = True
        for d in range(len(dungeon)) :
            if tatigue >= dungeon[d][0] :
                tatigue -= dungeon[d][1]
            else : 
                answer.append(d)
                state = False
                break
        if state :
            return len(dungeon)
    
    return max(answer)


a = [[80,20],[50,40],[30,10]]


print(solution(80, a))