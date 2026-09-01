# 정수 내림차순으로 배치하기


def solution(n):
  answer = "".join(sorted(str(n), reverse=True))
  # sorted(list | str | tuple) : 원본 변경, None 반환
  # array.sort() : 원본 유지, 새로운 리스트 반환

  return int(answer)
