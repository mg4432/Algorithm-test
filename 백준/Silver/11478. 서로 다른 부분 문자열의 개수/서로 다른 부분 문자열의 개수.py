s = input() 
lst = [] 

len_s = len(s)
for loc in range(0, len_s) :
    for k in range(1, len_s + 1 - loc) : 
        val = s[loc:loc+k]
        lst.append(val)

print(len(set(lst)))