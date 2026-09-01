# 두 정수 사이의 합


def solution(a, b):
  answer = 0
  list = []

  if a == b:
    return a
  elif a > b:
    list = range(b, a + 1)
  elif b > a:
    list = range(a, b + 1)

  for item in list:
    answer += item

  return answer


def solution2(a, b):
  return sum(range(min(a, b), max(a, b) + 1))
