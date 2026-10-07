# 게임 맵 최단거리 [깊이 / 너비 우선탐색(DFS/BFS)]

from collections import deque


# 0은 벽이 있는 자리, 1은 벽이 없는 자리
def solution(maps):
  n, m = len(maps), len(maps[0])

  q = deque()
  q.append((0, 0))

  visited = [[False for _ in range(m)] for _ in range(n)]

  dx = [1, -1, 0, 0]
  dy = [0, 0, -1, 1]
  # delta = [(1,0), (-1,0), (0,-1), (0,1)]

  while q:
    x, y = q.popleft()
    visited[x][y] = True

    if x == n - 1 and y == m - 1:
      return maps[n - 1][m - 1]

    for i in range(4):  # 4가지 방향 (오른쪽 1, 왼쪽 1, 위로 1, 아래로 1)
      nx, ny = dx[i] + x, dy[i] + y

      if nx >= 0 and ny >= 0 and nx < n and ny < m:
        if maps[nx][ny] == 1 and not visited[nx][ny]:
          maps[nx][ny] = maps[x][y] + 1
          visited[nx][ny] = True
          q.append((nx, ny))

  return -1
