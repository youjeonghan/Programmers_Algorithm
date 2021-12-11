# 레벨1     연습문제        2016년
from collections import defaultdict


def solution(a, b):
    day = {0: "SUN", 1: "MON", 2: "TUE", 3: "WED", 4: "THU", 5: "FRI", 6: "SAT"}
    dic = defaultdict(int)
    for i in range(1, 12 + 1):
        if i <= 7:
            if i % 2 == 1:
                dic[i] = 31
            else:
                dic[i] = 30
        else:
            if i % 2 == 1:
                dic[i] = 30
            else:
                dic[i] = 31
    dic[2] = 29
    today = sum([dic[i] for i in range(1, a)]) + b
    return day[(today + 4) % 7]


if __name__ == "__main__":
    print(solution(1, 1))
