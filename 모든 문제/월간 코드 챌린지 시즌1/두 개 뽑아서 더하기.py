# 레벨1     월간 코드 챌린지 시즌1      두 개 뽑아서 더하기
from itertools import combinations


def solution(numbers):
    temp = combinations(numbers, 2)
    result = [x + y for x, y in temp]
    return sorted(set(result))


if __name__ == "__main__":
    print(solution([2, 1, 3, 4, 1]))
