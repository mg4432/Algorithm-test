def solution(arr1, arr2):
    nr = len(arr1) 
    nc = len(arr2[0])
    arr2 = list(zip(*arr2))
    
    ret = [[0 for _ in range(nc)] for _ in range(nr)]
    
    for i in range(nr) : 
        for j in range(nc) : 
            val =  sum([x*y for x, y in zip(arr1[i], arr2[j])])
            ret[i][j] = val
    return  ret