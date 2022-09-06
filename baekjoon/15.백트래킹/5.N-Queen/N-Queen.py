N = int(input())
pos = [-1 for _ in range(N)]
prev_x = [-1 for _ in range(N)]

def check_queen_position(x, y) :
    for pos_y, pos_x in enumerate(pos) :
        sub_y = y - pos_y
        if pos_y == -1 :
            return True
        
        if (pos_x == x or 
            (abs(y - sub_y) == pos_y and abs(x - sub_y) == pos_x) or
            (abs(y - sub_y) == pos_y and abs(x + sub_y) == pos_x)) :
            return False
    return True

for y in range(N) :
    for x in range(N) :
        
        if check_queen_position(x, y) :
            pos[y] = x
            prev_x[y] = x
            break
        
    if pos[y] == -1 :    
        pos[y-1] = -1
        y -= 1
    