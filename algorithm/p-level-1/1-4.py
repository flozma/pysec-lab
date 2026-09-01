# 자연수 뒤집어 배열로 만들기


def solution(n):
  # answer = [int(item) for item in list(reversed(str(n)))]
  answer = list(map(int, reversed(str(n))))

  return answer
