# 레벨2     월간 코드 챌린지 시즌3      n^2 배열 자르기
# 20분 소요


def solution(n, left, right):
    result = []
    for i in range(left, right + 1):
        div_num = i // n
        result.append(div_num + 1 if div_num >= i % n else i % n + 1)
    return result


if __name__ == "__main__":
    print(solution(3, 2, 5))
