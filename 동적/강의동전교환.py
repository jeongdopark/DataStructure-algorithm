

n = int(input())
coin = list(map(int, input().split()))
coin.sort()
num = int(input())

mm = [1000] * (num +1)
mm[0] = 0

for i in range(n):
    for j in range(coin[i], num + 1):
        mm[j] = min(mm[j], mm[j-coin[i]] +1)
print(mm)