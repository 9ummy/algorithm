# 1260번: DFS와 BFS
# https://www.acmicpc.net/problem/1260

# 큐 사용을 위한 라이브러리 임포트
from collections import deque

# 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V
N, M, V = map(int, input().split())

# 인접 리스트 형태로 그래프 생성
graph = [[] for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

# 근접 노드 번호가 작은 순서부터 오도록 정렬
for v in graph:
    # 파이썬 리스트의 sort 메소드는 원본 리스트를 정렬한다는 점 주의
    v.sort()


# 정답 출력을 위한 리스트
dfs_result = []
bfs_result = []


def dfs(graph, v, visited):
    # 현재 노드를 방문처리
    visited[v] = True
    # 방문한 노드를 출력
    # print(v, end=' ')
    dfs_result.append(str(v))
    # 현재 노드와 연결된 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    # 시작 노드를 큐에 넣고 탐색 시작
    queue = deque([start])
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐의 최하단 노드를 꺼내고 출력
        v = queue.popleft()
        # print(v, end=' ')
        bfs_result.append(str(v))
        # 해당 노드의 근접 노드를 돌면서
        for i in graph[v]:
            # 방문하지 않았을 경우
            if not visited[i]:
                # 모두 큐에 넣어주고 방문 처리함
                queue.append(i)
                visited[i] = True


# DFS 함수 호출
visited = [False for _ in range(N+1)]
dfs(graph, V, visited)

# BFS 함수 호출
visited = [False for _ in range(N+1)]
bfs(graph, V, visited)

# 정답 출력
print(' '.join(dfs_result))
print(' '.join(bfs_result))
