from collections import deque 
def solution(s):
    answer = True
    
    l, r = deque([]), deque(list(s)) 
    
    while r : 
        if len(l) == 0 : 
            l.append(r.popleft()) 
            
        else : 
            val = r.popleft() 
            if val == '(' : 
                l.append(val)
            else : 
                if l[-1] == '(' : 
                    l.pop() 
                else : 
                    l.append(val)
                    
    if l : 
        return False 
    else : 
        return True 
    
    
    