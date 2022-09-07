N = int(input())
pos = [-1 for _ in range(N)]
prev_x = [-1 for _ in range(N)]
result = 0
x_start = 0

if N == 1 : 
    print('1')
    exit()
def check_queen_position(x, y) :
    for pos_y, pos_x in enumerate(pos) :
        sub_y = abs(y - pos_y)
        sub_x = abs(x - pos_x)
        if pos_x == -1 :
            return True
        
        if (pos_x == x or sub_x == sub_y) :
            return False
    return True

def remove_prev(x, y) :
    pos[y-1] = -1
    
y = 0
recrusion = 0
number_type = ''
if N % 2 == 0 :
    number_type = 'even'
    recrusion = N // 2
else :
    number_type = 'odd'
    recrusion = (N // 2) + 1
    
while y < N :
    if pos[0] >= recrusion :
        break
    for x in range(x_start, N) :
        
        if check_queen_position(x, y) :
            pos[y] = x
            prev_x[y] = x
            break
        
    if pos[y] == -1 :
        if y == 0 and x_start == N:
            break
        x_start = pos[y-1] + 1
        pos[y-1] = -1
        y -= 1
        
    elif pos[-1] != -1 :
        x_start = pos[y-1] + 1
        pos[y] = -1
        pos[y-1] = -1
        y -= 1
        if number_type == 'even' :
            result += 2
        else :
            if pos[0] == recrusion-1 :
                result += 1
            else :
                result += 2
            
    
    elif pos[y] != -1 :
        y += 1
        x_start = 0
        
print(result)