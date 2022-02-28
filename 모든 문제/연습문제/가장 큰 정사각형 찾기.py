# 레벨2     연습 문제       가장 큰 정사각형 찾기
# DP
# 다시 풀기 (효율성 실패)
# 31분 소요


def solution(board):
    y_len, x_len = len(board), len(board[0])
    square_len = min(y_len, x_len)
    for n in range(square_len, 0, -1):
        for i in range(y_len):
            if i + n > y_len:
                break
            for j in range(x_len):
                if j + n > x_len:
                    break
                result = check(board, i, j, n)
                if result:
                    return n ** 2
    return 0


def check(board, y, x, n):
    for i in range(y, y + n):
        for j in range(x, x + n):
            if board[i][j] == 0:
                return False
    return True


if __name__ == "__main__":
    print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
