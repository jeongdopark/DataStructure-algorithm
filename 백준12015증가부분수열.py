


n = int(input())
num = list(map(int,input().split()))
ans = 0

memo = [0] * n
memo[0] = 1
for i in range(1, n):
    max = 0
    for j in range(i):
        if(num[i] > num[j] and max < memo[j]):
            max = memo[j]
    memo[i] = max + 1
    if(ans < memo[i]):
        ans = memo[i]
print(ans)            