def solution(lottos, win_nums):
    answer = []
    rank = [6,6,5,4,3,2,1]
    rank_num = 0
    
    for lotto in lottos :
        if lotto in win_nums :
            rank_num += 1
    answer.append(rank[rank_num + lottos.count(0)])
    answer.append(rank[rank_num])
    
    
    return answer