

# n, w = map(int, input().split())
# e = [list(map(int,input().split())) for _ in range(n)]
# maxV = [0] * (w+1)
# ans = 0
# for i in e:
#     for j in range(i[0], w+1):
#         maxV[j] = max(maxV[j], i[1] + maxV[j-i[0]])
#     if(ans < maxV[j]):
#         ans = maxV[j]

        

n, m = map(int, input().split())
dy = [0] * (m+1)
for i in range(n):
    w, v = map(int, input().split())
    for j in range(w, m+1):
        dy[j] = max(dy[j], dy[j-w] + v)
print(dy[m])