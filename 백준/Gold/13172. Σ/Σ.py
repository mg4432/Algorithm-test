import math 

def f(a, b, c) : 
    if b == 1 : 
        return a % c
    else : 
        rec = f(a, b//2, c)
        if b % 2 == 0 : 
            return rec**2%c
        else : 
            return a*rec*rec%c

def mod(n) : 
    m = 1000000007
    return f(n, m-2, m)
    
def operation(a, b) : 
    gcd_value = math.gcd(a, b) 
    a //= gcd_value
    b //= gcd_value 

    return b * mod(a) % 1000000007

n = int(input()) 
lst = [] 

for _ in range(n) : 
    lst.append(list(map(int, input().split()))) 

answer = 0 

for l in lst : 
    answer += operation(l[0], l[1])

print(answer%1000000007)