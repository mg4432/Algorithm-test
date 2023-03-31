from collections import Counter 
def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine)
    counter = sorted(counter.items(), key = lambda item : item[1], reverse = True)
    for key, val in counter : 
        k -= val
        answer += 1 
        if k <= 0 : 
            break
        
    
    return answer