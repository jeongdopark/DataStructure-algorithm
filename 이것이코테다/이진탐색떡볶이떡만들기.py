

n, m = map(int, input().split())

num = list(map(int, input().split()))
num.sort()

def binary(array, target, start, end):
    ans = 0
    while start <= end:
        count = 0
        
        mid = (start + end) // 2
        for i in array:
            if(i - mid > 0):
                count += (i - mid)
        if(count >= target):
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    return ans

print(binary(num, m, 1, num[-1]))


        