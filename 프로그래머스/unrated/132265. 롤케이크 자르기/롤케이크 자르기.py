from collections import Counter 

def solution(topping):
    answer = 0
    dict_l = {top : 0 for top in set(topping)}
    dict_r = Counter(topping)

    unique_l = []
    unique_r = list(set(topping))
    
    for top in topping :      
        dict_l[top] += 1 
        if dict_l[top] == 1:
            unique_l.append(top)
        dict_r[top] -= 1
          
        if dict_r[top] == 0 :
            unique_r.remove(top)
        
        if len(unique_l) == len(unique_r) : 
            answer += 1
        
        if len(unique_l) > len(unique_r) : 
            break
        
        # print(dict_l, dict_r)
    return answer