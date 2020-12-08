

n, m, k = map(int, input().split())

numList = list(map(int, input().split()))

numList.sort()

count = 0
sum = 0
while count != 8:
    for _ in range(k):
        sum += numList[-1]
        count += 1
        if(count == 8):
            break
    if(count != 8):
        sum += numList[-2]
        count += 1

print(sum)