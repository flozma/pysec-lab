# 자릿수 더하기 [연습문제]


def solution(n):
  answer = 0

  for char in str(n):
    answer += int(char)

  return answer
