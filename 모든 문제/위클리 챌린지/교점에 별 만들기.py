# 레벨2     위클리 챌린지       교점에 별 만들기
# 더 깔끔하게 풀기 가능


def solution(line):
    x_range = [float("inf"), -float("inf")]
    y_range = [float("inf"), -float("inf")]
    dot_list = set()
    for i in line:
        for j in line:
            denominator = i[0] * j[1] - i[1] * j[0]
            if denominator == 0:
                continue
            x = (i[1] * j[2] - i[2] * j[1]) / denominator
            y = (i[2] * j[0] - i[0] * j[2]) / denominator
            if not x.is_integer() or not y.is_integer():
                continue
            y, x = int(y), int(x)
            dot_list.add((y, x))
            x_range = [min(x_range[0], x), max(x_range[1], x)]
            y_range = [min(y_range[0], y), max(y_range[1], y)]

    gp = [["."] * int(x_range[1] + 1 - x_range[0]) for _ in range(int(y_range[1] + 1 - y_range[0]))]
    for i in dot_list:
        gp[i[0] - y_range[0]][i[1] - x_range[0]] = "*"

    for i in range(len(gp)):
        gp[i] = "".join(gp[i])
    return list(reversed(gp))


if __name__ == "__main__":
    print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
