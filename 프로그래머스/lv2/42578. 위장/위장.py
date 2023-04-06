def solution(clothes):
    answer = 1
    clothes_dict = {} 
    
    for c in clothes : 
        name = c[0]
        cat = c[1]
        if clothes_dict.get(cat, False) : 
            clothes_dict[cat] += 1 
            
        else : 
            clothes_dict[cat] = 1
            
    for _, v in clothes_dict.items() : 
        answer *= (v+1) 
    return answer - 1