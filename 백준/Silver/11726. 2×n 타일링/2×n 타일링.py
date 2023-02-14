n = int(input())
cache = [0 for index in range(1001)]
cache[1], cache[2] = 1, 2
for index in range(3, 1001) : 
    cache[index] = cache[index - 1] + cache[index - 2]

print(cache[n] % 10007)