def solution(progresses, speeds):
    answer = []
    
    while progresses : 
        if progresses[0] >= 100 : 
            cnt = 0 
            while progresses and progresses[0] >= 100 : 
                cnt += 1 
                progresses.pop(0)
                speeds.pop(0)
            answer.append(cnt)
        else : 
            progresses = [x + add for x, add in zip(progresses, speeds)]
            
        
    return answer
# import math 

# def solution(progresses, speeds) : 
#     answer = [] 
#     take_times = [math.ceil((100-x)/y) for x, y in zip(progresses, speeds)]
    
#     done = []
    
#     while take_times : 
#         val = take_times.pop(0) 
#         if not done :
#             done.append(val) 
#         else : 
#             if done[-1] >= val : 
#                 done.append(val) 
#             else : 
#                 answer.append(len(done)) 
#                 done = [val]
                
#     if done : 
#         answer.append(len(done)) 
        
#     return answer