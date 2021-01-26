

n = int(input())
nList = list(map(int, input().split()))
nList.sort()
m = int(input())
mList = list(map(int, input().split()))


def binary(array, target, start, end):
    
    while start <= end:
        mid = (start + end) // 2
        if(array[mid] == target):
            return mid
        elif(array[mid] > target):
            end = mid - 1
        else:
            start = mid + 1
    return None
    
for i in mList:
    result = binary(nList, i, 0, n-1)
    if(result != None):
        print("yes", end = ' ')
    else:
        print("no", end = ' ')