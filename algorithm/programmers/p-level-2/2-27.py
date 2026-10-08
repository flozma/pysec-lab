# 튜플 [2019 카카오 개발자 겨울 인턴십]


def solution(s):
  answer = []

  s = s[2:-2].split("},{")
  _s = sorted(s, key=lambda x: len(x))

  for int_arr in [list(map(int, char.split(","))) for char in _s]:
    for i in answer:
      if i in int_arr:
        int_arr.remove(i)
    answer.append(int_arr[0])

  return answer
