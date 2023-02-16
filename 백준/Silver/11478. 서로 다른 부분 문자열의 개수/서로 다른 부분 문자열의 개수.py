s = input() 
lst = [] 

for sp in range(0, len(s)) :
    for k in range(1,len(s)+1-sp) : 
        val = s[sp:sp+k]
        lst.append(val)

print(len(list(set(lst))))