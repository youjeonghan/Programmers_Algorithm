# 3레벨     위클리 챌린지       퍼즐 조각 채우기
# 73분 소요

from collections import deque


def solution(game_board, table):
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def dfs(y, x, f, nf, board):
        temp = []
        sx = sy = float("inf")
        bx = by = 0
        deq = deque([(y, x)])
        board[y][x] = nf
        while deq:
            y, x = deq.popleft()
            temp.append([y, x])
            sy, sx = min(sy, y), min(sx, x)
            by, bx = max(by, y), max(bx, x)
            for dy, dx in d:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == f:
                    board[ny][nx] = nf
                    deq.append((ny, nx))
        result = [[0] * (bx - sx + 1) for _ in range(by - sy + 1)]
        for ty, tx in temp:
            result[ty - sy][tx - sx] = 1
        return result

    def rotate(arr):
        return [list(i) for i in zip(*arr[::-1])]

    n = len(game_board)
    board_li, block_li = [], []
    for y in range(n):
        for x in range(n):
            if game_board[y][x] == 0:
                board_li.append(dfs(y, x, 0, 1, game_board))
            if table[y][x] == 1:
                block_li.append(dfs(y, x, 1, 0, table))

    block_check = [0] * len(block_li)
    for i in board_li:
        flag = 0
        for j in range(len(block_li)):
            block = block_li[j]
            l1, l2 = len(i), len(i[0])
            r1, r2 = len(block), len(block[0])
            if block_check[j] == 0 and ((l1 == r1 and l2 == r2) or (l1 == r2 and l2 == r1)):
                for _ in range(4):
                    if i == block:
                        block_check[j] = 1
                        flag = 1
                        break
                    i = rotate(i)
            if flag == 1:
                break

    answer = 0
    for i in range(len(block_check)):
        if block_check[i] == 1:
            answer += sum(sum(block_li[i], []))

    return answer


if __name__ == "__main__":
    print(
        solution(
            [
                [1, 1, 0, 0, 1, 0],
                [0, 0, 1, 0, 1, 0],
                [0, 1, 1, 0, 0, 1],
                [1, 1, 0, 1, 1, 1],
                [1, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 0, 0],
            ],
            [
                [1, 0, 0, 1, 1, 0],
                [1, 0, 1, 0, 1, 0],
                [0, 1, 1, 0, 1, 1],
                [0, 0, 1, 0, 0, 0],
                [1, 1, 0, 1, 1, 0],
                [0, 1, 0, 0, 0, 0],
            ],
        )
    )
