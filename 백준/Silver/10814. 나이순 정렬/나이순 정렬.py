import sys 
n = int(input()) 
lst = [] 
for _ in range(n) : 
    age, name = sys.stdin.readline().split()
    lst.append([int(age), name])
    
lst.sort(key = lambda x : x[0])

for l in lst : 
    print(l[0], l[1])