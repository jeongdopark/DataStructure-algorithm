


n = int(input())

for _ in range(n):
    total = 0
    count = 0
    num = list(map(int, input().split()))
    for i in range(1, len(num)):
        total += num[i]
    average = total / (len(num) - 1)
    for i in range(1, len(num)):
        if(average < num[i]):
            count += 1
    rate = (count / (len(num) - 1) * 100)
    print(f'{rate:.3f}%')