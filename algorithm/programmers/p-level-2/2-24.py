# 전화번호 목록 [해시]


def solution1(phone_book):
  phone_book.sort()

  for i in range(len(phone_book) - 1):
    word1 = phone_book[i]
    word2 = phone_book[i + 1]

    if word2[: len(word1)] == word1:
      return False

  return True


# 해시 풀이
def solution2(phone_book):
  answer = True
  hash_map = {}
  for phone_number in phone_book:
    hash_map[phone_number] = 1

  for phone_number in phone_book:
    temp = ""

    for number in phone_number:
      temp += number
      if temp in hash_map and temp != phone_number:
        answer = False
  return answer
