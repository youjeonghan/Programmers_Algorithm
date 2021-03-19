from sys import stdin
from math import ceil

read = stdin.readline
n, k = map(int, read().rstrip().split())
li = list(map(int, read().rstrip().split()))
_min = min(li)

check = len(li)
for i in li:
    if i == _min:
        check -= 1

print(ceil(check / (k - 1)))


# 2번
# from sys import stdin
# from math import ceil

# read = stdin.readline
# t = int(read())

# for _ in range(t):
#     n, m = map(int, read().split())
#     sum = n + m
#     cnt = 0
#     for i in range(n // 5):
#         if sum < 12:
#             break
#         cnt += 1
#         sum -= 12

#     print(cnt)
