# 2606번: 바이러스
# https://www.acmicpc.net/problem/2606

from collections import deque

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for v in graph:
    v.sort()


def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])
    result = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                result += 1
    return result


visited = [False for _ in range(N+1)]

print(bfs(graph, 1, visited))
