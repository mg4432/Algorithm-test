def solution(s):
    stack = [] 
    
    for letter in s :
        if not stack :
            stack.append(letter)
        else : 
            if stack[-1] == letter : 
                stack.pop()
            else : 
                stack.append(letter)
        
    return 0 if stack else 1