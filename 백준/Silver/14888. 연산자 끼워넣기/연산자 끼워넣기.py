def cal(numbers, operations) :
    nums, ops = numbers.copy(), operations.copy() 
    ret = nums.pop(0)
    
    while ops : 
        op = ops.pop(0)
        next_value = nums.pop(0)
        if op == '+' : 
            ret += next_value

        elif op == '-' : 
            ret -= next_value 

        elif op == '*' : 
            ret *= next_value 

        else : 
            if ret < 0 : 
                ret = -(-ret//next_value)
            else : 
                ret //= next_value
    return ret
        
n = int(input()) 
numbers = list(map(int, input().split()))
operations = list(map(int, input().split()))
ref = ['+','-','*','/']
for i in range(4) : 
    val = operations.pop(0)
    for j in range(val) : 
        operations.append(ref[i])

from itertools import permutations 

Max = -1000000001
Min = 1000000001

for p in permutations(operations, len(operations)) : 
    p = list(p)
    val = cal(numbers, p)
    if val > Max : 
        Max = val
    if val < Min : 
        Min = val

print(Max, Min)