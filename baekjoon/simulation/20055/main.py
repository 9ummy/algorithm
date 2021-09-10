# 한 줄에 두 개 입력 받기
n, k = map(int, input().split())
# 한 줄에 여러 개 입력 받아서 리스트로 만들기
durability = list(map(int, input().split()))
# 특정 값을 특정 개수만큼 가지게 리스트 초기화
robots = [0 for i in range(n)]

answer = 0


def shouldStop(list):
    check = [i for i, v in enumerate(durability) if v == 0]
    if len(check) >= k:
        return True
    else:
        return False


while not shouldStop(durability):
    # 단계 시작
    answer += 1

    # 컨베이어 벨트 회전
    # 마지막 내구도(2n - 1)를 첫 번째로 옮겨줌
    tmp = durability.pop(n * 2 - 1)
    durability.insert(0, tmp)

    # 벨트 위의 로봇도 옮겨줌
    robots.pop()
    robots.insert(0, 0)
    # 벨트가 움직여 로봇이 내리는 위치(n - 1)에 도착한 경우 로봇을 즉시 내림
    if robots[n - 1] == 1:
        robots[n - 1] = 0

    # 로봇이 벨트 위에서 이동함
    # 로봇들의 이동 후 위치를 기록할 임시 리스트
    if 1 in robots:
        # for i, v in enumerate(robots):
        for i in range(n - 2, -1, -1):

            # # 벨트 위에 로봇이 있고 & 다음 칸에는 로봇이 없으며 & 다음 칸의 내구도가 0이 아닌 경우 이동
            if robots[i] == 1 and robots[i + 1] == 0 and durability[i + 1] != 0:
                robots[i] = 0
                robots[i + 1] = 1
                durability[i + 1] -= 1

            # 로봇이 컨베이어 벨트의 제일 마지막 칸으로 이동한 경우 로봇을 즉시 내림
            if robots[n - 1] == 1:
                robots[n - 1] = 0

    # 올리는 지점 내구도가 남아있을 경우 로봇을 올린다
    if durability[0] != 0:
        robots[0] = 1
        durability[0] -= 1


print(answer)
