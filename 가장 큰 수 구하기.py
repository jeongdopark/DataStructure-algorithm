


a, b = map(str, input().split())
num = list(a)
b = int(b)
c=b
count = 0
lt = 0

for _ in range(len(a)):
    for j in range(lt+1, b+1+lt):
        if(int(num[lt]) < int(num[j])):
            num.pop(lt)
            b -= 1
            break
    else:
        lt += 1
    if(b == 0 or len(a)-c == lt):
        for _ in range(b):
            num.pop()
        break
for i in num:
    print(i, end = '')