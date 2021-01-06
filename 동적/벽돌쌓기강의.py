
n = int(input())

num = [list(map(int, input().split())) for _ in range(n)]
num = sorted(num, key = lambda x : x[0])

dy = [0] * 20
ans = 0
for i in range(n):
    dy[i+1] = num[i][1]

for i in range(1, n):
    max = 0
    for j in range(i):
        if(num[i][2] > num[j][2] and max < dy[j+1]):
            max = dy[j+1]
    dy[i+1] = max + num[i][1]
    if( ans < dy[i+1]):
        ans = dy[i+1]
    
print(ans)