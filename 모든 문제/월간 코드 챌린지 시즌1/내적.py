# 레벨1 월간 코드 챌린지 시즌1        내적


def solution(a, b):
    return sum(map(lambda x, y: x * y, a, b))


if __name__ == "__main__":
    print(solution([1, 2, 3, 4], [-3, -1, 0, 2]))
