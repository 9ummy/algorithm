#
# 9184번: 신나는 함수 실행
# https://www.acmicpc.net/problem/9184
#

# 메모이제이션 방식 풀이
pairs = []

while True:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break

    pairs.append((a, b, c))


# 메모이제이션에 활용할 딕셔너리 초기화
memo = {}


def w(a, b, c):
    # 종료 조건
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        if (20, 20, 20) not in memo:
            memo[(20, 20, 20)] = w(20, 20, 20)
        return memo[(20, 20, 20)]

    if a < b and b < c:
        if (a, b, c-1) not in memo:
            memo[(a, b, c-1)] = w(a, b, c-1)
        if (a, b-1, c-1) not in memo:
            memo[(a, b-1, c-1)] = w(a, b-1, c-1)
        if (a, b-1, c) not in memo:
            memo[(a, b-1, c)] = w(a, b-1, c)
        return memo[(a, b, c-1)] + memo[(a, b-1, c-1)] - memo[(a, b-1, c)]

    if (a-1, b, c) not in memo:
        memo[(a-1, b, c)] = w(a-1, b, c)
    if (a-1, b-1, c) not in memo:
        memo[(a-1, b-1, c)] = w(a-1, b-1, c)
    if (a-1, b, c-1) not in memo:
        memo[(a-1, b, c-1)] = w(a-1, b, c-1)
    if (a-1, b-1, c-1) not in memo:
        memo[(a-1, b-1, c-1)] = w(a-1, b-1, c-1)
    return memo[(a-1, b, c)] + memo[(a-1, b-1, c)] + memo[(a-1, b, c-1)] - memo[(a-1, b-1, c-1)]


for pair in pairs:
    (a, b, c) = pair
    print(f"w{pair} = {w(a, b, c)}")
