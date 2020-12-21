



n, m = map(int, input().split())
length = list(map(int, input().split()))


def count(len):
    cnt = 0
    for i in length:
        if(i - len >= 0):
            cnt += (i - len)
    return cnt


lt = 1
rt = max(length)
ans = 0
while lt <= rt:
    mid = (lt + rt) // 2 
    if(count(mid) >= m):
        ans = mid
        lt = mid +1
    else:
        rt = mid - 1
print(ans)

