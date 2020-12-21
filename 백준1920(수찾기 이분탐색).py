

n = int(input())
num1 = list(map(int, input().split()))
num1.sort()
m = int(input())
num2 = list(map(int, input().split()))

for i in num2:
    lt = 0
    rt = n-1
    while lt <= rt:
        mid = (lt + rt) // 2
        if(i > num1[mid]):
            lt = mid + 1
        elif(i < num1[mid]):
            rt = mid - 1
        if(i == num1[mid]):
            print(1)
            break
    else:
        print(0)
            
          