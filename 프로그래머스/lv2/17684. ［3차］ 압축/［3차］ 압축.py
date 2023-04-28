from collections import deque 
from string import ascii_uppercase

def solution(msg):
    answer = []
    lst = list(ascii_uppercase)
    Dict = {lst[i]  : (i+1) for i in range(26)} 
    idx = 27
    added = '' 
    msg = deque(list(msg))
    
    while msg : 
        added = msg.popleft()
        while msg : 
            to_add = msg.popleft() 
            added += to_add
            if added not in Dict :
                answer.append(Dict[added[:-1]])
                Dict[added] = idx
                idx += 1 
                added = to_add
    
    answer.append(Dict[added])
    return answer