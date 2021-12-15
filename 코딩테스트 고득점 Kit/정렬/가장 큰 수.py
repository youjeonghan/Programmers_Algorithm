# 레벨2     정렬        가장 큰 수


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 4, reverse=True)
    return str(int("".join(numbers)))


if __name__ == "__main__":
    print(solution([3, 30, 34, 5, 9]))
