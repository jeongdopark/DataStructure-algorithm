

n = int(input())
num = list(map(int, input().split()))
mm = [0] * n
mm[0] = 1
ans = 0
for i in range(1, n):
    max = 0
    for j in range(i):
        if(num[i] > num[j]):
            if(max < mm[j]):
                max = mm[j]
    mm[i] = max + 1
    if(mm[i] > ans):
        ans = mm[i]

print(ans)