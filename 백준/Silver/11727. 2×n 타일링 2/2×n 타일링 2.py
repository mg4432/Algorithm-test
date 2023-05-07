n = int(input()) 
lst = [0 for _ in range(1001)]

lst[1] = 1 
lst[2] = 3 
lst[3] = 5 

for i in range(4, 1001) : 
    lst[i] = lst[i-2] * 2 + lst[i-1]
    
print(lst[n] % 10007)