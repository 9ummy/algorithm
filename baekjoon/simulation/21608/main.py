#
# 21608번: 상어 초등학교
# https://www.acmicpc.net/problem/21608
#


n = int(input())
room = [[0] * (n + 1) for _ in range(n + 1)]

#     좌  우  하  상
dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]

likes = [list(map(int, input().split())) for _ in range(n * n)]

r = c = 1

# 2차원 배열 탐색
for x in range(1, n + 1):
    for y in range(1, n + 1):

        # 탐색하며 각 자리마다 인접한 자리
        for i in range(4):
            nr = x + dr[i]
            nc = y + dc[i]


for i in room:
    print(i)

print(likes)
