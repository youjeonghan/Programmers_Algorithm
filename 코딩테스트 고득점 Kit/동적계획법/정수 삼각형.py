# 3레벨     코딩테스트 고득점 Kit     정수 삼각형
def solution(triangle):
    for floor in range(1, len(triangle)):
        for idx in range(len(triangle[floor])):
            if idx == 0:
                triangle[floor][idx] += triangle[floor - 1][idx]
            elif idx == len(triangle[floor]) - 1:
                triangle[floor][idx] += triangle[floor - 1][idx - 1]
            else:
                triangle[floor][idx] += max(triangle[floor - 1][idx], triangle[floor - 1][idx - 1])

    return max(triangle[-1])


if __name__ == "__main__":
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
