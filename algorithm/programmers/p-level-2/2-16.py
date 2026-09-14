# 영어 끝말잇기 [Summer/Winter Coding(~2018)]
def solution(n, words):
  iteration = 1

  # 탈락하는 사람의 번호, 해당 사람이 몇번째 차례에 탈락하는지
  # 탈락하는 사람이 없다면 [0,0] 반환
  for pos in range(1, len(words)):
    if words[pos - 1][-1] != words[pos][0] or words[pos] in words[:pos]:
      return [pos % n + 1, iteration]

    if (pos + 1) % n == 0:
      iteration += 1

  return [0, 0]
