
# 투 포인터를 사용함

n = list(input().split())
n = list(map(int, n))


left = 0
right = len(n) -1
volume = 0
leftMax = n[left]
rightMax = n[right]
while left < right:
    leftMax = max(n[left], leftMax)
    rightMax = max(n[right], rightMax)

    if(n[left] < n[right]):
        volume += leftMax - n[left]
        left += 1
    else:
        volume += rightMax - n[right]
        right -= 1
print(volume)
