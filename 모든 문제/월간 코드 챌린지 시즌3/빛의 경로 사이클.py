# 레벨2     월간 코드 챌린지 시즌3      빛의 경로 사이클


def solution(grid):
    li = [list(i) for i in grid]
    gp = [[[1] * len(li[0]) for _ in range(len(li))] for _ in range(4)]

    result = []
    for k in range(4):
        for i in range(len(li)):
            for j in range(len(li[0])):
                if gp[k][i][j]:
                    result.append(dfs(li, gp, (k, i, j)))
    return sorted(result)


def dfs(li, gp, route):
    k, i, j = route
    cnt = 0
    x_len = len(li)
    y_len = len(li[0])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while gp[k][i][j]:
        gp[k][i][j] = 0
        cnt += 1
        if li[i][j] == "S":
            pass
        elif li[i][j] == "L":
            k = (4 + k - 1) % 4
        elif li[i][j] == "R":
            k = (4 + k + 1) % 4
        i = (i + dx[(4 + k - 2) % 4]) % x_len
        j = (j + dy[(4 + k - 2) % 4]) % y_len
    return cnt


if __name__ == "__main__":
    print(solution(["SL", "LR"]))
