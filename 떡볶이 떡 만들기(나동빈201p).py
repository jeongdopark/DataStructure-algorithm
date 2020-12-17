

n, m = map(int, input().split())
testList = list(map(int, input().split()))
testList.sort()
answer = 0


def cut(array, start, end, target):
    global answer
    
    
    while start <= end:
        # count 변수를 while문 스코프 밖에 설정해서 답이 이상했었다 mid초기화시 count는 누적되는 현상 발생
        count = 0 
        mid = (start + end) // 2
        for i in array:
            if(i > mid):
                count += (i - mid)
            else:
                continue
        if(count > target):
            start = mid + 1
        elif(count < target):
            end = mid - 1
        elif(count == target):
            answer = mid
            start = mid + 1
    return answer

print(cut(testList,testList[0], testList[-1], m))
            
                
