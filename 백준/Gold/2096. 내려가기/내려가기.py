import sys 

n = int(input()) 

max_cur = [0, 0, 0]
max_add = [0, 0, 0]

min_cur = [0, 0, 0]
min_add = [0, 0, 0]

for i in range(n) : 
    a, b, c = map(int, sys.stdin.readline().split()) 
    max_add[0] = a + max(max_cur[0], max_cur[1])
    max_add[1] = b + max(max_cur[0], max_cur[1], max_cur[2])
    max_add[2] = c + max(max_cur[1], max_cur[2])

    min_add[0] = a + min(min_cur[0], min_cur[1])
    min_add[1] = b + min(min_cur[0], min_cur[1], min_cur[2])
    min_add[2] = c + min(min_cur[1], min_cur[2])

    for i in range(3) : 
        max_cur[i] = max_add[i]
        min_cur[i] = min_add[i] 

print(max(max_cur), min(min_cur))