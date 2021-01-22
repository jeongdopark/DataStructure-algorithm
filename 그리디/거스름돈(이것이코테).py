

n = int(input())

num = [500, 100, 50, 10]
count = 0
for i in range(4):
    if(n >= num[i]):
        count += n // num[i]
        n = n % num[i]
print(count)