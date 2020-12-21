

a = int(input())
b = int(input())
c = int(input())

result = list(str(a * b * c))


memo = [0] * 10

for i in result:
    memo[int(i)] += 1
    

for i in range(10):
    print(memo[i])