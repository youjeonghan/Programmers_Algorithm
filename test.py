def solution(board):
    n = len(board)
    opened = [(0, 0, -1, 0)]  # y, x, direction, cost
    closed = [[-1 for _ in range(n)] for _ in range(n)]

    answer = -1
    while opened:
        y, x, d, c = opened.pop(0)
        if (y, x) == (n - 1, n - 1) and (answer == -1 or answer > c):
            answer = c

        neighbors = [(y, x - 1), (y, x + 1), (y - 1, x), (y + 1, x)]
        for direction, (ny, nx) in enumerate(neighbors):
            # boundary
            if ny <= -1 or ny >= n or nx <= -1 or nx >= n:
                continue

            # wall
            if board[ny][nx]:
                continue

            # visited and cheaper
            cost = c + (100 if d == direction or d == -1 else 600)
            if closed[ny][nx] != -1 and closed[ny][nx] < cost:
                continue

            opened.append((ny, nx, direction, cost))
            closed[ny][nx] = cost

    print(closed)
    return answer


if __name__ == "__main__":
    print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))