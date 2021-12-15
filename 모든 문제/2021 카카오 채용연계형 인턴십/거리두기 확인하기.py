# 레벨2     2021 카카오 채용연계형 인턴십       거리두기 확인하기

from collections import deque


def solution(places):
    li = []
    for i in places:
        tmp = [list(j) for j in i]
        li.append(tmp)

    result = []
    for i in li:
        result.append(check(i))
    return result


def check(li):
    for i in range(5):
        for j in range(5):
            if li[i][j] == "P":
                gp = [[1] * 5 for _ in range(5)]
                gp[i][j] = 0
                stack = deque([(i, j, 0)])
                if bfs(li, gp, stack) == 0:
                    return 0

    return 1


def bfs(li, gp, stack):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while stack:
        x, y, cnt = stack.popleft()
        for q in range(4):
            nx, ny = x + dx[q], y + dy[q]
            if 0 <= nx < 5 and 0 <= ny < 5 and gp[nx][ny] and li[nx][ny] != "X":
                if li[nx][ny] == "P":
                    return 0
                gp[nx][ny] = 0
                if cnt + 1 < 2:
                    stack.append((nx, ny, cnt + 1))
    return 1


if __name__ == "__main__":
    print(
        solution(
            [
                [
                    "POOOP",
                    "OXXOX",
                    "OPXPX",
                    "OOXOX",
                    "POXXP",
                ],
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
            ]
        )
    )
