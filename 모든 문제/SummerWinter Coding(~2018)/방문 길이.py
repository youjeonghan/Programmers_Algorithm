# 레벨2     Summer/Winter Coding(~2018)     방문 길이
# 19분 40초 소요

from collections import defaultdict


def solution(dirs):
    y, x = 0, 0
    cnt = 0
    check = defaultdict(lambda: defaultdict(lambda: 0))
    for i in dirs:
        if i == "U":
            dy, dx = y - 1, x
        elif i == "D":
            dy, dx = y + 1, x
        elif i == "L":
            dy, dx = y, x - 1
        elif i == "R":
            dy, dx = y, x + 1

        if -5 <= dy <= 5 and -5 <= dx <= 5:
            if check[(y, x)][(dy, dx)] == 0:
                cnt += 1
                check[(y, x)][(dy, dx)] = 1
                check[(dy, dx)][(y, x)] = 1
            y, x = dy, dx
    return cnt


if __name__ == "__main__":
    print(solution("UD"))
