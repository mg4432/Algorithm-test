from itertools import permutations

n = int(input()) 
k = int(input())
lst = [] 

for _ in range(n) : 
    lst.append(input()) 

lst = list(lst) 

answer = []
for p in permutations(lst, k) : 
    s = ''.join(p)
    if s not in answer : 
        answer.append(s) 

print(len(answer))

