"""
DFS(Depth First Search) : Root Node에서 시작해 깊숙히 들어가 확인한 뒤 다른 루트를 탐색하는 방식

- 모든 노드를 방문하고자 할 때 사용
- BFS보다 간단 (BFS에 비해 검색속도가 느림)
- Stack 사용
"""


def DFS(graph, start, visited):
  # start는 시작위치
  visited[start] = True
  print(start, end=" ")

  # 현재 노드와 연결된 노드를 재귀적으로 호출
  for i in graph[start]:
    if not visited[i]:
      DFS(graph, i, visited)


if __name__ == "__main__":
  graph = [
    [],
    [2, 3, 7],  # 1번 노드에 인접한 노드들
    [1, 4, 6],  # 2번 노드에 인접한 노드들
    [1, 5, 7],  # 3번 노드에 인접한 노드들
    [2, 6],  # 4번 노드에 인접한 노드들
    [3, 7],  # 5번 노드에 인접한 노드들
    [2, 4],  # 6번 노드에 인접한 노드들
    [1, 3],  # 7번 노드에 인접한 노드들
  ]

  # 노드를 방문한 정보를 1차원 리스트로 표현
  visited = [False] * 8

  print("방문순서 with DFS")
  DFS(graph=graph, start=1, visited=visited)
