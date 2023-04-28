def solution(x, y, n) : 
    cnt = 0 
    s = set() 
    s.add(x) 
    
    while s : 
        if y in s : 
            return cnt
        s_next = set() 
        
        for i in s :
            if i+n <= y : 
                s_next.add(i+n)
            if i*2 <= y : 
                s_next.add(i*2)
            if i*3 <= y : 
                s_next.add(i*3)

        s = s_next
        cnt += 1
    
    return -1 