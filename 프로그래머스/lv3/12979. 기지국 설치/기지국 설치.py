import math 

def solution(n, stations, w):
    answer = 0
    can_cover = 2*w + 1
    covered = 0
    for s in stations : 
        if covered >= s : 
            pass
        to_cover = s - w - covered - 1
        covered = s + w 
        answer += math.ceil(to_cover/can_cover)
        
    if covered >= n : 
        return answer 
    
    else : 
        answer += math.ceil((n-covered)/can_cover)
        return answer