def solution(n):
    return len([x for x in range(1, n+1) if n%x == 0 and x % 2 == 1])