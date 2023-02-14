from collections import deque 
import sys

n = int(input()) 
lst = deque() 

for _ in range(n) :
    s = list(sys.stdin.readline().strip().split())
    if len(s) == 1 : 
        if s[0] == 'pop' : 
            if len(lst) == 0 : 
                print('-1')
            else : 
                print(lst.popleft())

        elif s[0] == 'size' : 
            print(len(lst))

        elif s[0] == 'empty' : 
            if len(lst) == 0 :
                print('1')
            else : 
                print('0')

        elif s[0] == 'front': 
            if len(lst) > 0 : 
                print(lst[0])
            else : 
                print('-1')

        elif s[0] == 'back': 
            if len(lst) > 0 : 
                print(lst[-1])
            else : 
                print('-1')

    else : 
        lst.append(int(s[1]))

