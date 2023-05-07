import sys 
n, m = map(int, input().split()) 
lst = list(map(int, input().split()))
for i in range(1, len(lst)) : 
    lst[i] += lst[i-1]
lst = [0] + lst

for _ in range(m) : 
    s, e = map(int, sys.stdin.readline().split())
    print(lst[e] - lst[s-1])
