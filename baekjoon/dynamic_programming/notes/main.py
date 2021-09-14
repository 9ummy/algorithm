#
# 피보나치 수열을 계산하는 3가지 방법
#

# 1. 재귀 함수 사용

def fibo_recursive(x):
    # 종료 조건
    if x == 1 or x == 2:
        return 1

    return fibo_recursive(x - 1) + fibo_recursive(x - 2)


print(fibo_recursive(4))

# 재귀 함수의 경우 x가 커지게 될 경우 동일한 연산을 반복 (중복되는 부분 문제)
# O(2^n)의 시간 복잡도


# 2. 메모이제이션(탑다운) 사용

# 탑다운으로 연산된 값을 저장하기 위한 리스트
dp_top_down = [0] * 100


def fibo_top_down(x):
    # 종료 조건
    if x == 1 or x == 2:
        return 1

    # 이미 연산된 결과가 있다면 연산 결과를 리턴
    if dp_top_down[x] != 0:
        return dp_top_down[x]

    # 아직 계산하지 않은 문제라면 계산해서 dp 테이블에 저장
    dp_top_down[x] = fibo_top_down(x - 1) + fibo_top_down(x - 2)

    return dp_top_down[x]


print(fibo_top_down(99))


# 3. 바텀업 사용
dp_bottom_up = [0] * 100

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
dp_bottom_up[1] = 1
dp_bottom_up[2] = 1
n = 99

# 3부터 99까지 피보나치 수를 계산해서 dp 테이블에 저장
for i in range(3, n + 1):
    dp_bottom_up[i] = dp_bottom_up[i - 1] + dp_bottom_up[i - 2]

print(dp_bottom_up[n])
