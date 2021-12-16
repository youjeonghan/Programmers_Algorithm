# 레벨2     정렬        H-Index
# 43분 소요
# 더 깔끔한 해답 존재

from collections import defaultdict


def solution(citations):
    dic = defaultdict(int)
    for i in citations:
        dic[i] += 1
    li = list(zip(dic.keys(), dic.values()))
    li.sort(reverse=True)
    acc = 0
    len_li = len(citations)
    result = []
    for i, cnt in li:
        acc += cnt
        if acc >= len_li / 2 and acc <= i:
            result.append(min(acc, i))
    return max(result) if len(result) else 0


if __name__ == "__main__":
    print(solution([88, 89]))
    print(solution([3, 0, 6, 1, 5]))
    print(solution([0, 0, 0]))
