n = int(input())

cache = [10000 for _ in range(5001)]
    
cache[3] = 1 
cache[5] = 1 


for idx in range(6, 5001) : 
    
    cache[idx] = min(cache[idx-3], cache[idx-5]) + 1
    
print(cache[n] if cache[n] < 10000 else -1)