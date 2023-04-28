from collections import deque 

def check(s) : 
    l, r = deque(), deque(s)
    while r : 
        val = r.popleft() 
        if not l : 
            l.append(val)
        else : 
            if (l[-1] == '[' and val == ']')  or (l[-1] == '{' and val == '}') or (l[-1] == '(' and val == ')')  :
                l.pop()
            else : 
                l.append(val)
                
    if len(l)+len(r) == 0 : 
        return True 
    else : 
        return False
                
        
def solution(s):
    answer = 0
    s = deque(list(s))
    for i in range(len(s)) : 
        s.rotate(1) 
        if check(s) : 
            answer += 1 
        
    return answer