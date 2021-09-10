from collections import deque

# 보드 크기 입력 받기
n = int(input())

# 입력 받은 크기대로 보드 생성
# board = [[0] * (n + 1) for _ in range(n + 1)]
# apple = [[0] * (n + 1) for _ in range(n + 1)]

# DON'T

# coordinate = []
# for _ in range(k):
#   coordinate.append(list(map(int, input().split())))

# t = int(input())
# moves = []
# for _ in range(t):
#   moves.append(list(map(str, input().split())))

# DO
# 사과 좌표와 방향 변환 입력 받기
apples = [list(map(int, input().split())) for _ in range(int(input()))]
moves = [list(map(str, input().split())) for _ in range(int(input()))]
moves = deque(moves)

snake = deque([[1, 1]])

r = snake[-1][0]
c = snake[-1][1]

seconds = 0
direction = 'R'

# 뱀의 진행 방향에 따라 방향 전환을 판단하는 함수


def rotate(cur, change):
    current_direction = cur

    if current_direction == 'R':
        if change == 'D':
            current_direction = 'D'
        else:
            current_direction = 'U'
    elif current_direction == 'L':
        if change == 'D':
            current_direction = 'U'
        else:
            current_direction = 'D'
    elif current_direction == 'U':
        if change == 'D':
            current_direction = 'R'
        else:
            current_direction = 'L'
    elif current_direction == 'D':
        if change == 'D':
            current_direction = 'L'
        else:
            current_direction = 'R'

    return current_direction


while (r >= 1 and r <= n and c >= 1 and c <= n):
    seconds += 1

    # 현재 진행 방향에 따라 이동하기
    # 이동하려는 위치가 board 범위에서 벗어나면 while문 멈춤
    if direction == 'R':
        c += 1
    elif direction == 'D':
        r += 1
    elif direction == 'L':
        c -= 1
    elif direction == 'U':
        r -= 1

    # snake 리스트에 뱀 머리 위치 추가해주기
    # 이동하려는 위치가 board 범위 벗어나지 않더라도 몸통과 부딪히면 while문 멈춤
    if [r, c] in snake:
        break
    else:
        snake.append([r, c])

    # 꼬리를 삭제해야할지 판단하기 위해
    # 이동하려는 칸에 사과가 있는지 확인
    if [r, c] in apples:
        # 사과가 있다면 꼬리를 지우지 않고 사과 리스트에 포함된 해당 좌표만 삭제해줌
        apples.pop(apples.index([r, c]))
    else:
        # 사과가 없다면 뱀 꼬리 좌표 삭제
        snake.popleft()

    # 방향 전환을 해야할지 판단
    if len(moves) != 0 and int(moves[0][0]) == seconds:
        # 방향 전환
        direction = rotate(direction, moves[0][1])
        # 전환 마친 후 moves에서 삭제
        moves.popleft()


print(seconds)
