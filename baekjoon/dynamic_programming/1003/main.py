#
# 1003번: 피보나치 함수
# https://www.acmicpc.net/problem/1003
#

# 바텀업 방식 풀이

n = int(input())
numbers = [int(input()) for _ in range(n)]

# 정답 배열을 담을 리스트 초기화
# 인덱스가 0부터 40까지 들어갈 수 있도록 길이 41인 리스트 생성
answer = [(0, 0)] * 41
answer[0] = (1, 0)
answer[1] = (0, 1)

for i in range(2, 41):
    (a1, b1) = answer[i - 1]
    (a2, b2) = answer[i - 2]
    answer[i] = (a1 + a2, b1 + b2)

for number in numbers:
    (a, b) = answer[number]
    print(a, b)
