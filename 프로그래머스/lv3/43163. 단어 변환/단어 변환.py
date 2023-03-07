from collections import deque 

def check(a, b) : 
    tmp_lst = [1 if w_a != w_b else 0 for w_a, w_b in zip(list(a), list(b))]
    if sum(tmp_lst) == 1 : 
        return True 
    else : 
        return False
    
    
def solution(begin, target, words):
    answer = 0
    q = deque([begin]) 
    visited = {w : 0 for w in words}
    cnt = 0
    while q : 
        cnt += 1 
        for i in range(len(q)) : 
            check_word = q.popleft() 
            visited[check_word] = 1 
            for i in range(len(words)) : 
                word = words[i]

                if check(check_word, word) and visited[word] == 0 : 
                    q.append(word)

                    print(check_word, word, cnt, q)
            if target in q : 
                return cnt 

    return 0