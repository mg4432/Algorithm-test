def solution(num, total):
    answer = []
    
    div, mod = divmod(total, num)
    if mod == 0 : 
        Range = (num-1)//2
        for r in range(Range+1) :
            answer.append(div-r)
            answer.append(div+r)
    
    else : 
        answer.append(div)
        answer.append(div+1)
        Range = (num-2)//2 
        for r in range(Range+1) :
            answer.append(answer[0]-r)
            answer.append(answer[1]+r)
            
    return sorted(list(set(answer)))