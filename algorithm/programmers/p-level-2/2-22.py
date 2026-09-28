# H-index [정렬]


def solution(citations):
  n = len(citations)
  index = n

  while index > 0:
    # h번 이상의 논문을 모았다면, 자동으로 그 밖의 논문들은 h번 미만
    # lower_quote를 모을 필요 없음
    over_quote = [citation for citation in citations if citation >= index]

    if len(over_quote) >= index:
      return index

    index -= 1

  return 0
