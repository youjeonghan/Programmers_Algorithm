# 2020 KAKAO BLIND RECRUITMENT  순위 검색
from collections import defaultdict
from itertools import product
from bisect import bisect_left


def solution(info, query):
    dic = defaultdict(list)

    for item in info:
        item = item.split()
        slot = []
        for i in range(4):
            slot.append({"-", item[i]})
        for i in product(*slot):
            dic["".join(i)].append(int(item[4]))

    for k in dic.keys():
        dic[k].sort()

    result = []
    for q in query:
        q = q.replace(" and ", " ").split(" ")
        score = int(q[-1])
        q = q[:-1]

        t = dic["".join(q)]
        result.append(len(t) - bisect_left(t, score))

    return result


if __name__ == "__main__":
    print(
        solution(
            [
                "java backend junior pizza 150",
                "python frontend senior chicken 210",
                "python frontend senior chicken 150",
                "cpp backend senior pizza 260",  #
                "java backend junior chicken 80",
                "python backend senior chicken 50",
            ],
            [
                "java and backend and junior and pizza 100",
                "python and frontend and senior and chicken 200",
                "cpp and - and senior and pizza 250",
                "- and backend and senior and - 150",
                "- and - and - and chicken 100",
                "- and - and - and - 150",
            ],
        )
    )
