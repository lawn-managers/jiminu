def solution(numbers, hand):
    answer = ''
    
    left_hand = '*'
    right_hand = '#'
    
    left_line = [1,4,7,'*']
    right_line = [3,6,9,'#']
    center_line = [2,5,8,0]
    
    for number in numbers :
        if number in left_line :
            left_hand = number
            answer += 'L'
        elif number in right_line :
            right_hand = number
            answer += 'R'
        else :
            left_move = 0
            right_move = 0
            if left_hand not in left_line :
                left_index = center_line.index(left_hand)
            else :
                left_index = left_line.index(left_hand)
                left_move += 1
            if right_hand not in right_line :
                right_index = center_line.index(right_hand)
            else :
                right_index = right_line.index(right_hand)
                right_move += 1
                
            center_index = center_line.index(number)
            
            left_move += abs(left_index - center_index)
            right_move += abs(right_index - center_index)
            
            if left_move < right_move :
                left_hand = number
                answer += 'L'
            elif right_move < left_move :
                answer += 'R'
                right_hand = number
            elif left_move == right_move :
                if hand == 'left' :
                    answer += 'L'
                    left_hand = number
                elif hand == 'right' :
                    answer += 'R'
                    right_hand = number
    
    return answer