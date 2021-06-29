# 2020 카카오 인턴십    경주로 건설
# 다시
# 결국 힌트 얻고 품
from collections import deque


def solution(board):
    size = len(board[0])
    visit = [[-1] * size for _ in range(size)]
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # y,x 위, 오른쪽, 아래, 왼쪽
    result = []

    def bfs():
        q = deque([[0, 0, 0, (0, 0)]])
        while q:
            y, x, cost, od = q.popleft()
            for i in range(4):
                ny = y + d[i][0]
                nx = x + d[i][1]
                money = 100 if od == d[i] or cost == 0 else 600  # 전과 같은 방향이거나 시작 +100 / 코너 +600
                ncost = cost + money
                if (
                    (0 <= ny < size and 0 <= nx < size)  # 경계
                    and board[ny][nx] == 0  # 벽 아님
                    and (visit[ny][nx] == -1 or visit[ny][nx] >= ncost)  # 처음오거나 더 좋은 비용의 길
                ):
                    visit[ny][nx] = ncost
                    q.append([ny, nx, ncost, d[i]])

    bfs()
    return visit[-1][-1]


if __name__ == "__main__":
    print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
