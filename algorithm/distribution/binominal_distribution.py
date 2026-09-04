import numpy as np

# 20번 동전 던지기에서 앞면이 나오는 횟수
n = 20
p = 0.5

print(np.random.binomial(n, p, size=10))
