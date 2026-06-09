"""
n = 5
res = n * (n + 1) * (2 * n + 1) // 6
print(res)
"""

"""
from functools import reduce

n = 5
res = reduce(lambda x, y: x + y * y, range(1, n + 1), 0)
print(res)
"""

n = 5
total = 0

for i in range(1, n + 1):
    total += i * i
print(total)