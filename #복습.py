


a, b = map(int, input().split())
num = []
for _ in range(a):
    num.append(int(input()))

num.sort()

def count(n):
    cnt = 1
    flag = num[0]
    for i in range(1, a):
        if(flag + n <= num[i]):
            flag = num[i]
            cnt += 1
    return cnt



lt = num[0]
rt = num[-1]
ans = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if(count(mid) < b):
        rt = mid - 1
    else:
        ans = mid
        lt = mid + 1

print(ans)