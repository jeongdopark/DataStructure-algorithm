# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
#  N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
n = int(input())
def test(n):
    count = 0
    if(1<= n < 100):
        count = n
        return count
    else: 
        # 100 <= n < 1000
        count = 99
        for i in range(100, n+1):
            num = list(str(i))
            if(int(num[0]) - int(num[1]) == int(num[1]) - int(num[2])):
                count += 1
        return count
print(test(n))

