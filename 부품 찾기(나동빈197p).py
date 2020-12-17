

import math
n = int(input())
nList = list(map(int, input().split()))
m = int(input())
mList = list(map(int, input().split()))
nList.sort()
lt = 0
rt = n-1

def check(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if(array[mid] == target):
            return print('yes')
        elif(array[mid] > target):
            end = mid - 1
        else:
            start = mid + 1
    return print('no')


for i in mList:
    check(nList, i, lt, rt)
