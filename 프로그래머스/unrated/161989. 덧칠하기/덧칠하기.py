def solution(n, m, section):
    answer = 1
    
#     while section : 
#         cur = section[0] 
#         covered = cur + m 
#         section = [s for s in section if s >= covered]
        
#         answer += 1
#         if not section : 
#             break
    now = section[0]
    end = now + m - 1
    for s in section[1:] : 
        if s <= end : 
            pass 
        else : 
            now = s 
            end = now + m - 1 
            answer += 1
        
    return answer