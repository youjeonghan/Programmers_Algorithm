# 2021 KAKAO BLIND RECRUITMENT  순위 검색
from collections import defaultdict
from bisect import bisect_left


def solution(info, query):
    dic = defaultdict(
        lambda: defaultdict(
            lambda: defaultdict(
                lambda: defaultdict(list),
            ),
        ),
    )

    for item in info:
        item = item.split()
        dic[item[0]][item[1]][item[2]][item[3]].append(int(item[4]))

    def score_check(d, q):
        result = 0
        d.sort()
        return len(d) - bisect_left(d, int(q[4]))

    def pc_check(d, q):
        if q[3] == "-":
            result = 0
            for k in d.keys():
                result += score_check(d[k], q)
            return result
        else:
            return score_check(d[q[3]], q)

    def js_check(d, q):
        if q[2] == "-":
            result = 0
            for k in d.keys():
                result += pc_check(d[k], q)
            return result
        else:
            return pc_check(d[q[2]], q)

    def bf_check(d, q):
        if q[1] == "-":
            result = 0
            for k in d.keys():
                result += js_check(d[k], q)
            return result
        else:
            return js_check(d[q[1]], q)

    def language(d, q):
        if q[0] == "-":
            result = 0
            for k in dic.keys():
                result += bf_check(d[k], q)
            return result
        else:
            return bf_check(d[q[0]], q)

    result = []
    for st in query:
        q = st.split(" and ")
        temp = q[-1].split(" ")
        q[-1] = temp[0]
        q.append(temp[1])
        result.append(language(dic, q))

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
