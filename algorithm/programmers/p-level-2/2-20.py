# n^2 배열 자르기 [월간 코드 챌린지 시즌 3]


def solution_before(n, left, right):
  """시간복잡도가 매우 커지므로, 시간 초과 문제 발생"""
  matrix = [[0] * n for i in range(n)]

  for i in range(n):
    for j in range(n):
      if i != j:
        matrix[i][j] = (i + 1) if i > j else (j + 1)
      else:
        matrix[i][j] = i + 1

  array = sum(matrix, [])

  return array[left : right + 1]


def solution(n, left, right):
  return [max(index // n, index % n) + 1 for index in range(left, right + 1)]
