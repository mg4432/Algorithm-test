def solution(n):
    answer = 0
    if n == 1 : 
        return 1 
    dp = [0 for i in range(n+1)]
    dp[1] = 1 
    dp[2] = 2 
    
    for i in range(3, n+1) : 
        dp[i] = dp[i-1] + dp[i-2]
    return divmod(dp[-1], 1234567)[1]