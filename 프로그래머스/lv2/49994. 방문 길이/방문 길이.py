def solution(dirs):
    answer = 0
    cur_loc = [0, 0]
    
    s = []
    
    for d in dirs : 
        next_loc = cur_loc.copy()
        if d == 'U' : 
            if cur_loc[1] < 5 :
                next_loc[1] += 1 
            
        elif d == 'D' : 
            if cur_loc[1] > -5 :
                next_loc[1] -= 1 
            
        elif d == 'R' : 
            if cur_loc[0] < 5 :
                next_loc[0] += 1 
            
        elif d == 'L' : 
            if cur_loc[0] > -5 :
                next_loc[0] -= 1  

        if cur_loc != next_loc : 
            if cur_loc + next_loc not in s and next_loc + cur_loc not in s : 
                answer += 1
                s.append(cur_loc + next_loc)
                s.append(next_loc + cur_loc)
        cur_loc = next_loc
    return answer