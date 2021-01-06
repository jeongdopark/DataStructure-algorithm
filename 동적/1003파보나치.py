# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.
# 각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.


cnt0 = [1, 0]
cnt1 = [0, 1]

for i in range(2, 41):
    cnt0.append(cnt0[i-1] + cnt0[i-2])
    cnt1.append(cnt1[i-1] + cnt1[i-2])

for _ in range(int(input())):
    n = int(input())
    print(cnt0[n], cnt1[n])
