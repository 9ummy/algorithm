# 문자열을 이용한 방식
# 메모리 초과로 실패

n, k = map(int, input().split())

circle = ''.join(list(str(i) for i in range(1, n + 1)))

# K번째 사람을 카운트
count = 0

# 요세푸스 순열을 기록할 리스트
answer = []

head = circle[:k - 1]


while len(circle) > 0:

    if len(circle) == 1:
        target = 0
    elif len(circle) < k:
        target = k % len(circle) - 1
    else:
        target = k - 1

    answer.append(circle[target])

    head = circle[:target]
    tail = circle[target + 1:]
    circle = tail + head

    print(f"answer: {answer} target: {target} circle: {circle}")

print(f"<{', '.join(answer)}>")
