from collections import deque 
import sys 

def bfs(value) : 
    q = deque([value]) 
    while q : 
        v = q.popleft() 
        if v == k : 
            return visited[v]
        for next_value in (v-1, v+1, 2*v) : 
            if 0 <= next_value < 100001 and visited[next_value] == 0 :
                visited[next_value] = visited[v] + 1
                q.append(next_value)
                
n, k = map(int, sys.stdin.readline().split()) 
visited = [0] * 100001    
print(bfs(n))