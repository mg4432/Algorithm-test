def solution(s):
    answer = []
    lst = list(map(int, s.split())) 
    
    answer.append(str(min(lst)))
    answer.append(str(max(lst)))
    return ' '.join(answer)