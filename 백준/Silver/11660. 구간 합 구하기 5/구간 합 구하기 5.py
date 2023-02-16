import sys 
n, m = map(int, input().split()) 

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1) : 
    graph[i] = [0] + list(map(int, sys.stdin.readline().split())) 


for i in range(1, n+1) : 
    graph[1][i] += graph[1][i-1]
    graph[i][1] += graph[i-1][1]


for i in range(2, n+1) : 
    for j in range(2, n+1) : 
        graph[i][j] += graph[i][j-1] + graph[i-1][j] - graph[i-1][j-1]

for _ in range(m) : 
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split()) 
    answer = graph[x2][y2] - graph[x1-1][y2] - graph[x2][y1-1] + graph[x1-1][y1-1]
    print(answer)