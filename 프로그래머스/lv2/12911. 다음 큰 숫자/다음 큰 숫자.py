def solution(n):
    answer = 0
    i = 1
    cnt = bin(n)[2:].count('1')
    while True : 
        val = n + i 
        Bin = bin(val)[1:]
        if Bin.count('1') == cnt : 
            break
        i += 1
    return val