from collections import deque 
def solution(t, p):
    answer = 0
    N = len(p) 
    t = deque(list(t))
    
    for _ in range(len(t) - N + 1) : 
        lst = list(t)[:N]
        if int(''.join(lst)) <= int(p) :
            answer += 1
        t.rotate(-1)
    return answer