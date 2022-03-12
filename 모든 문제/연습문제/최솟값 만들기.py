# 2레벨     연습문제        최솟값 만들기
# 4분 30초 소요


def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=False)

    return sum([a * b for a, b in zip(A, B)])


if __name__ == "__main__":
    print(solution([1, 4, 2], [5, 4, 4]))
