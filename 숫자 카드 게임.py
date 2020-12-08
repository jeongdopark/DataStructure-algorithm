

n, m = map(int, input().split())
minimum = []

for _ in range(n):
    k = list(map(int, input().split()))
    k.sort()
    minimum.append(k[0])

print(max(minimum))
