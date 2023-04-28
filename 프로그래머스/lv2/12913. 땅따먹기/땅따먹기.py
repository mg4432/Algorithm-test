def solution(land):
    answer = 0
    nc = len(land[0])
    
    for i in range(1, len(land)) : 
        for j in range(len(land[0])) : 
            land[i][j] += max([land[i-1][k] for k in range(nc) if k != j])

    return max(land[-1])