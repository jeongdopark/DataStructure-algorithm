
#  que로 풀이

from collections import deque

dir = list(input())
n = int(input())

for i in range(n):
    same = []
    classList = list(map(str, input()))
    classList = deque(classList)
    while(len(classList) > 0):
        if(classList[0] in dir):
            cur = classList.popleft()
            same.append(cur)
        else:
            classList.popleft()
    if(dir == same):
        print('#%d YES' %(i+1))
    else:
        print('#%d NO' %(i+1))