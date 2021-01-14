

n = int(input())
num = list(map(int, input().split()))
m = int(input())
num.sort()

mm = [0] * (m+1)

for i in range(n):
    for j in range(num[i], m+1):
        mm[j] = mm[j-num[i]] + 1
print(mm[m])

