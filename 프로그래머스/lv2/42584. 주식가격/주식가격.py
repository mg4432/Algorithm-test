def solution(prices):
    answer = [0 for i in range(len(prices))]
    for i in range(len(prices)-1) :
        sec = 0
        for j in range(i+1, len(prices)) : 
            sec += 1
            if prices[i] > prices[j] : 
                break
                
        answer[i] = sec 
        
    return answer