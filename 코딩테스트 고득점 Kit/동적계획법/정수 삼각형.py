# 3레벨     코딩테스트 고득점 Kit     정수 삼각형


def solution(triangle):
    _max = 0
    for floor, list in enumerate(triangle):
        if floor == len(triangle) - 1:
            break
        for idx, item in enumerate(list):
            if idx == 0:
                triangle[floor + 1][idx] += item
            elif idx == len(list) - 2:
                triangle[floor + 1][idx + 1] += item
            else:
                triangle[floor + 1][idx] += item
                triangle[floor + 1][idx + 1] += item

    return max(triangle[-1])


if __name__ == "__main__":
    print(
        solution(
            [
                [7],
                [3, 8],
                [8, 1, 0],
                [2, 7, 4, 4],
                [4, 5, 2, 6, 5],
            ]
        )
    )
    print(
        solution(
            [
                [7],
            ]
        )
    )
    print(
        solution(
            [
                [7],
            ]
        )
    )
