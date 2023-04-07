N = int(input()) 
num = list(map(int, input().split())) 
op = list(map(int, input().split()))

Max, Min = -1e9, 1e9

def dfs(depth, total, plus, minus, multi, div) : 
    global Max, Min 
    if depth == N : 
        Max = max(total, Max) 
        Min = min(total, Min)

    if plus : 
        dfs(depth + 1, total + num[depth], plus - 1, minus, multi, div)
    
    if minus : 
        dfs(depth + 1, total - num[depth], plus, minus - 1, multi, div)

    if multi : 
        dfs(depth + 1, total * num[depth], plus, minus, multi- 1, div)

    if div : 
        dfs(depth + 1, int(total/num[depth]), plus, minus, multi, div- 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(Max)
print(Min)