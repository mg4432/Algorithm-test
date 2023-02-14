import sys
read = sys.stdin.readline

cache = [0, 1, 1, 1, 2, 2] + [0 for _ in range(100)]

for i in range(6, 101):
    cache[i] = cache[i-1] + cache[i-5]

for _ in range(int(read())):
    print(cache[int(read())])