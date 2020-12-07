
# 투 포인터를 이용한 스왑

a = input()
list = []


for j in a:
    list.append(j)

left, right = 0, len(list)-1

while left < right:
    list[left], list[right] = list[right], list[left]
    left += 1
    right -= 1

print(list)