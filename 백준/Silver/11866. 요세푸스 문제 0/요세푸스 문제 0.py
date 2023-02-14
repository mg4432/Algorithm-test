from collections import deque
T, n = map(int, input().split())
lst = [(i+1) for i in range(T)]

q = deque(lst)
answer = []

while len(q) > 0 : 
    q.rotate(-(n-1))
    add = q.popleft()
    answer.append(add)
    
answer_ = ''
for s in answer : 
    answer_ += str(s) + ', '

print('<' + answer_[:-2] + '>')