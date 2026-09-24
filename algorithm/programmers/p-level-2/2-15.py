<<<<<<< HEAD
# 행렬의 곱셈 [연습문제]

def solution(arr1, arr2):
    m = len(arr1)
    n = len(arr1[0])
    r = len(arr2[0])
    
    answer = [[0 for _ in range(r)] for i in range(m)]
    
    for i in range(m):
        for k in range(r):
            for j in range(n):
                answer[i][k] += arr1[i][j] * arr2[j][k] 
    
    return answer
=======
# n개의 최소 공배수 [연습문제]
from math import gcd


# enumerate
def solution(arr):
  lcm = 0
  prev_num = arr[0]

  for index, value in enumerate(arr):
    if index != 0:
      lcm = prev_num * value // gcd(prev_num, value)
      prev_num = lcm
    else:
      prev_num = value

  return lcm


# plain arr
def solution2(arr):
  lcm = arr[0]

  for value in arr[1:]:
    lcm = (value * lcm) // gcd(value, lcm)

  return lcm


# gcd(a,b) = gcd(b,a mod b)
# 유클리드 호제법
def gcd_custom(a, b):
  while b != 0:
    a, b = b, a % b

  return a
>>>>>>> 8c2f13fa2c0a8766370d5038cadd9d02618b8a62
