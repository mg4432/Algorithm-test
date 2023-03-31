def solution(n, words):
    answer = [1, 1]
    cnt, Dict = 1, {}
    check = 0
    
    
    w0 = words[0][0]
    while True : 
        w1 = words.pop(0) 
        if w1 in Dict or w0[-1] != w1[0] :
            break 
        else : 
            Dict[w1] = 1 
        cnt += 1
        w0 = w1
        
        if len(words) == 0 : 
            answer = [0, 0]
            break
    
    if answer == [0, 0] :
        return answer 
    
    div, mod = divmod(cnt, n) 
    if mod == 0 : 
        answer[0] = n
        answer[1] = div
    else :
        answer[0] = mod
        answer[1] = div+1
           
    return answer