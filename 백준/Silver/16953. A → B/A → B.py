s, e = map(int, input().split())

cnt = 0 

while e > s : 
    cnt += 1
    if len(str(e)) >= 2 and str(e)[-1] == '1' : 
        e = int(str(e)[:-1])
    elif e % 2 == 0 : 
        e //= 2
    else : 
        cnt = -2
        break
if s == e : 
    print(cnt+1)
else : 
    print(-1)