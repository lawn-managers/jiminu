def make_dict(part, comp) :
    part_dict = {}
    comp_dict = {}
    for p in part :
        if p in part_dict :
            part_dict[p] = part_dict[p] + 1
        else :  
            part_dict[p] = 1
            
    for c in comp :
        if c in comp_dict :
            comp_dict[c] = comp_dict[c] + 1
        else :  
            comp_dict[c] = 1
    return part_dict, comp_dict

def solution(participant, completion):
    
    part, comp = make_dict(participant, completion)
    
    for p in part :
        if p in comp :
            # part[p] = part[p] - comp[p]
            if part[p] != comp[p] :
                return p
        else :
            return p
            
    # part_reverse = dict(map(reversed, part.items()))
    
    # answer = part_reverse[1]
    # return answer