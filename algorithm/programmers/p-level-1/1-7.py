# 하샤드 수


def solution(x):
  answer = x % sum(int(char) for char in str(x)) == 0
  # int(char) for char in str(x) # generator -> sum 과 함께 잘 씀
  # [int(char) for char in str(x)] # list

  return answer
