# 3레벨     위클리 챌린지       아이템 줍기
# 다시 풀기
# 그래프 2배로 만들어 풀어버리는 유형

from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)


def solution(rectangle, characterX, characterY, itemX, itemY):
    global answer
    answer = float("inf")
    gp = [[0] * 51 for _ in range(51)]
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1, x2 + 1):
            gp[i][y1] = 1
            gp[i][y2] = 1
        for i in range(y1, y2 + 1):
            gp[x1][i] = 1
            gp[x2][i] = 1

    for x1, y1, x2, y2 in rectangle:
        for x in range(x1 + 1, x2 - 1 + 1):
            for y in range(y1 + 1, y2 - 1 + 1):
                gp[x][y] = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    def dfs(x, y, n):
        global answer
        if x == itemX and y == itemY:
            answer = min(answer, n)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if gp[nx][ny]:
                gp[x][y] = 0
                print(nx, ny)
                dfs(nx, ny, n + 1)

    dfs(characterX, characterY, 0)
    return answer


if __name__ == "__main__":
    print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
