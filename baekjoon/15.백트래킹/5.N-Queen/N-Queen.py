N = int(input())

pos = [-1 for _ in range(N)]
result = 0
x_start = 0

# if N == 1 : 
#     print('1')
#     exit()
    
def check_queen_position(x, y) :
    for pos_y, pos_x in enumerate(pos) :
        sub_y = abs(y - pos_y)
        sub_x = abs(x - pos_x)
        if pos_x == -1 :
            return True
        
        if (pos_x == x or sub_x == sub_y) :
            return False
    return True
    
y = 0
recursion = 0
number_type = ''
state = True
if N % 2 == 0 :
    number_type = 'even'
    recursion = N / 2
else :
    number_type = 'odd'
    recursion = (N / 2)
    
while state :
    if pos[0] >= recursion :
        state = False
        result *= 2
    
    for x in range(x_start, N) :
        if check_queen_position(x, y) :
            pos[y] = x
            break
        
    if pos[y] == -1 :
        x_start = pos[y-1] + 1
        pos[y-1] = -1
        y -= 1
        
    elif pos[-1] != -1 :
        x_start = pos[y-1] + 1
        pos[y] = -1
        pos[y-1] = -1
        y -= 1
        result += 1
        
        # if pos[0] < recursion :
        #     result += 2
        # else : 
        #     result += 1
            
        # if number_type == 'even' :
        #     result += 2
        # else :
        #     if pos[0] == recursion-1 :
        #         result += 1
        #     else :
        #         result += 2
            
    
    elif pos[y] != -1 :
        y += 1
        x_start = 0
        
print(result)