from collections import deque

n, k = map(int, input().split())
circle = list(str(i) for i in range(1, n + 1))
circle = deque(circle)

answer = []

while len(circle) > 0:
    circle.rotate(k * -1 + 1)
    answer.append(circle.popleft())

print(f"<{', '.join(answer)}>")
