# 피로도 [완전탐색 DFS]


def DFS(answer, count, k, visited, dungeons):
  answer = max(answer, count)

  for i in range(len(dungeons)):
    if k < dungeons[i][0] or visited[i]:
      continue

    visited[i] = True

    answer = DFS(answer, count + 1, k - dungeons[i][1], visited, dungeons)

    # 방문처리 복원 -> 2번째는 또 다르게 방문할 것이므로 복원
    visited[i] = False

  return answer


def solution(k, dungeons):
  answer = 0

  visited = [False] * len(dungeons)
  count = 0  # dfs depth (방문한 개수)
  # k 피로도
  answer = DFS(answer, count, k, visited, dungeons)

  return answer
