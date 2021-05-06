def solution(board, moves):
    cnt = 0
    stack = []
    for loca in moves:
        dep = 0
        while dep != len(board[0]) - 1 and board[dep][loca - 1] == 0:
            dep += 1

        target = board[dep][loca - 1]
        board[dep][loca - 1] = 0
        if stack and stack[-1] == target:
            stack.pop()
            cnt += 2

        elif target != 0:
            stack.append(target)

    return cnt


if __name__ == "__main__":
    print(
        solution(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 3],
                [0, 2, 5, 0, 1],
                [4, 2, 4, 4, 2],
                [3, 5, 1, 3, 1],
            ],
            [1, 5, 3, 5, 1, 2, 1, 4],
        )
    )  # 4
