
from collections import deque

n, m = map(int, input().split())
dq = []

for i in range(n):
    dq.append(i + 1)
dq = deque(dq)
while len(dq) != 1:
    count = 0
    for i in range(m):
        if(count == m-1):
            dq.popleft()
        else:
            cur = dq.popleft()
            dq.append(cur)
            count  +=1
for j in dq:
    print(j)