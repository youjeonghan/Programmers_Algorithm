from bisect import bisect_left as bl

li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(bl(li, 5))
print(len(li) - bl(li, 5))
