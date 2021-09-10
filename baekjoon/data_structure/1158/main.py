# 리스트를 이용한 방식
# 시간초과 판정으로 실패


n, k = map(int, input().split())

circle = list(i for i in range(1, n + 1))

# K번째 사람을 카운트
count = 0

# 테이블에서 나간 사람의 인덱스를 체크할 리스트
check = []

# 요세푸스 순열을 기록할 리스트
answer = []


while len(answer) < n:

    for i, v in enumerate(circle):
        # 확인 중인 사람이 테이블에서 나간 사람이 아니라면 카운트 세기
        if i not in check:
            count += 1
        # 이미 테이블에서 나간 사람이라면 무시하고 다음 사람으로 넘어감
        else:
            continue

        # K번째 사람을 찾았다면
        # 테이블에서 나간 사람으로 표시하고
        # 정답 리스트에 추가
        if count == k:
            check.append(i)
            answer.append(str(v))
            count = 0

print(f"<{', '.join(answer)}>")
