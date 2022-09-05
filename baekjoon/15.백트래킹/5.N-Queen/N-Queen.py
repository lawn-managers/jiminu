N = int(input())
board = [[0 for _ in range(0, N)] for _ in range(N)]

queens = []
result = 0

for i in range(N) :
    queens.append([i, 0])

    for y in range(1, N) :
        
        pre_queens_num = len(queens)
        for x in range(N) :

            state = False
            for q in queens :
                
                if (abs(q[0]+x) == abs(q[1]+y) or abs(q[0]-x) == abs(q[1]-y) or q[0] == x) :
                    state = True
                    break
            
            if state :
                continue
            
            queens.append([x,y])
            break
        
        if pre_queens_num == len(queens) :
            queens.pop()
            y -= 1