from collections import deque 
def solution(priorities, location):
    answer = 0
    ps = sorted(priorities, reverse = True)
    queue = deque([[location, p] for location, p  in enumerate(priorities)])
    printed = 0 

    while queue : 
        val = queue.popleft()
        

        if val[1] >= ps[0] : 
            if val[0] == location :
                return printed + 1
            ps.pop(0)
            printed += 1
            
        else : 
            queue.append(val)
    return len(prioirites)