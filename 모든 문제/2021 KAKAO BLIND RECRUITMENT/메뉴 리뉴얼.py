from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    orders = [sorted(i) for i in orders]
    dic = defaultdict(int)
    count = [0] * 11
    for item in orders:
        for i in course:
            for j in list(combinations(list(item), i)):
                dic["".join(j)] += 1
                count[i] = max(count[i], dic["".join(j)])

    result = []
    for k, v in dic.items():
        if count[len(k)] == v and v > 1:
            result.append(k)
    result.sort()
    return result


if __name__ == "__main__":
    print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
