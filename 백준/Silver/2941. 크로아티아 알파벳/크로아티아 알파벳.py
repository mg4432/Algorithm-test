s = input().strip()
answer = 0
while s : 
    if s[:2] in ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z='] : 
        s = s[2:]
    
    elif s[:3] == 'dz=' : 
        s = s[3:]

    else : 
        s = s[1:]

    answer += 1 

print(answer)