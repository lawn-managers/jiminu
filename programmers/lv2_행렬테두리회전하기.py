import numpy as np

rows = 100
columns = 97
queries =[[1,1,100,97]]

def solution(rows, columns, queries):

    n = np.array(range(1, rows*columns+1)).reshape((rows,columns))
    answer = []
    
    for query in queries :
            x1 = query[0]-1
            y1 = query[1]-1
            x2 = query[2]-1
            y2 = query[3]-1
            
            rotate_list = []
            
            for i in range(y1, y2+1) :
                rotate_list.append(n[x1][i])
            for i in range(x1+1, x2+1) :
                rotate_list.append(n[i][y2])
            for i in range(y2-1, y1-1, -1) :
                rotate_list.append(n[x2][i]) 
            for i in range(x2-1, x1, -1) :
                rotate_list.append(n[i][y1])
            
            print(rotate_list)
            answer.append(min(rotate_list))
            
            for i in range(y1+1, y2+1) :
                n[x1][i] = rotate_list[0]
                del rotate_list[0]
            for i in range(x1+1, x2+1) :
                n[i][y2] = rotate_list[0]
                del rotate_list[0]
            for i in range(y2-1, y1-1, -1) :
                n[x2][i] = rotate_list[0]
                del rotate_list[0]
            for i in range(x2-1, x1-1, -1) :
                n[i][y1] = rotate_list[0]
                del rotate_list[0]
    answer = list(map(int, answer))
    return answer
solution(rows,columns,queries)