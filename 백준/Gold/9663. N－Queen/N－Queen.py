n = int(input()) 
board = [[0 for _ in range(n)] for _ in range(n)] 
answer = 0 

def dfs(row) : 
    global answer, n 
    # 마지막 행까지 탐색을 완료 
    if row == n : 
        answer += 1 
        return 

    dr, dc = [1, 1, 1], [-1, 0, 1]
    for col in range(n) : 
        if board[row][col] > 0 : 
            continue
        # 놓을 수 있음  
        for d in range(3) : 
            nr, nc = row + dr[d], col + dc[d]
            while nr < n and 0 <= nc < n : 
                board[nr][nc] += 1 
                nr += dr[d]
                nc += dc[d]

        dfs(row + 1) 

        # back tracking 
        for d in range(3) : 
            nr, nc = row + dr[d], col + dc[d]
            while nr < n and 0 <= nc < n : 
                board[nr][nc] -= 1 
                nr += dr[d]
                nc += dc[d]

dfs(0)
print(answer)
    

    
