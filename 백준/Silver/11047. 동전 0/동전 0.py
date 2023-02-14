n, k = map(int, input().split())
answer = 0
lst = [int(input()) for i in range(n)]

while True :
    m = lst.pop()
    if k >= m : 
        times, k = divmod(k, m)
        answer += times
    if k == 0 : 
        break
    
print(answer)
