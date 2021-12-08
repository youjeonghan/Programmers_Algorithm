# 1레벨     월간 코드 챌린지 시즌3      없는 숫자 더하기


def solution(numbers):
    return 45 - sum(set(numbers))


if __name__ == "__main__":
    print(solution([1, 2, 3, 4, 6, 7, 8, 0]))
