

board1 = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves1 = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0
    result = []
    
    for move in moves :
        for bo in board :
            if bo[move-1] != 0 :
                result.append(bo[move-1])
                bo[move-1] = 0
                break
        if len(result) >= 2 and result[-1] == result[-2] :
            result.pop()
            result.pop()
            answer += 2
    
    print(answer)
    return answer
  
solution(board1, moves1)