


n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]

info = sorted(info, key=lambda x : x[0])
h = [0] * n
h[0] = info[0][1]
ans = 0
for i in range(1, n):
    max = 0
    for j in range(i):
        if(info[i][2] > info[j][2] and max < h[j]):
            max = h[j]
    h[i] = max + info[i][1]        
    if(ans < h[i]):
        ans = h[i]
print(ans)        


