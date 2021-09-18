#
# 11053번: 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053
#

n = int(input())
sq = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if sq[i] > sq[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
