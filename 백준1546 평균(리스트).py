n = int(input())
num = list(map(int, input().split()))
newNum = max(num)

total = 0

for i in range(n):
    total += num[i]/newNum*100
print(total / n)

