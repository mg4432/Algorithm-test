n, m = map(int, input().split()) 
lst = [1 for i in range(m - n + 1)] 

for i in range(2, int(m**0.5)+1) : 
    sq = i ** 2 
    min_times = divmod(n-1, sq)[0] + 1
    for j in range(min_times * sq, m+1, sq) : 
        if  lst[j-n] == 1 : 
            lst[j-n] = 0

print(sum(lst))
