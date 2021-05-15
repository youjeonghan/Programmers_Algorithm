# 2레벨     코딩테스트 고득점 Kit     타겟 넘버
from itertools import product


def solution(numbers, target):
    print(list(product(["+", "-"], repeat=len(numbers))))


if __name__ == "__main__":
    print(solution([1, 1, 1, 1, 1], 3))