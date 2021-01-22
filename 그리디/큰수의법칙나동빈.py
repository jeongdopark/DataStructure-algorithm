


n, m, k = map(int, input().split())

num = list(map(int, input().split()))

num.sort()
ans = 0
while m != 0:
    print(m)
    for _ in range(k):
        ans += num[-1]
        m -= 1
        if(m == 0):
            break
    if(m == 0):
        break
    ans += num[-2]
    m -= 1

print(ans)