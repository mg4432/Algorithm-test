def factorial(n) :
    result = 1
    for i in range(1, n+1) :
        result *= i
    return result

def combination(n, r) : 
    return factorial(n) / (factorial(r) * factorial(n-r))
        
    
T = int(input())

for t in range(T) : 
    n, r = map(int, input().split())
    print(int(combination(r, n)))