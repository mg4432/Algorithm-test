from collections import deque 
def solution(elements):
    s = set() 
    n = len(elements)
    elements = deque(elements)
    
    for i in range(1, n+1) : 
        for j in range(n) : 
            elements.rotate(1)
            s.add(sum(list(elements)[:i]))
        
        
    return len(s)