# 레벨2     찾아라 프로그래밍 마에스터      게임 맵 최단거리
# 12분 해결

from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    gp = [[0] * m for _ in range(n)]

    stack = deque([[0, 0, 1]])

    while stack:
        x, y, cnt = stack.popleft()
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and gp[nx][ny] == 0:
                gp[nx][ny] = 1
                if nx == n - 1 and ny == m - 1:
                    return cnt + 1
                stack.append([nx, ny, cnt + 1])

    return -1


if __name__ == "__main__":
    print(
        solution(
            [
                [1, 0, 1, 1, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1],
                [1, 1, 1, 0, 1],
                [0, 0, 0, 0, 1],
            ]
        )
    )
