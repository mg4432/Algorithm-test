def solution(cookie):
    answer = 0
    n = len(cookie)
    
    for loc in range(n-1) :
        l_idx, l_sum = loc, cookie[loc]
        r_idx, r_sum = loc + 1, cookie[loc + 1]
        
        if l_sum == r_sum :
            answer = max(answer, l_sum)

        while l_idx >= 0 and r_idx < n : 
            if l_sum > r_sum : 
                r_idx += 1
                if r_idx < n : 
                    r_sum += cookie[r_idx]
                    if l_sum == r_sum :
                        answer = max(answer, l_sum)
            else : 
                l_idx -= 1 
                if l_idx >= 0 : 
                    l_sum += cookie[l_idx]
                    if l_sum == r_sum :
                        answer = max(answer, l_sum)
            
    return answer