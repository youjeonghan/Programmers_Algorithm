# 연습문제  광고 삽입
# 다시


def solution(n):
    answer = ""
    while n > 0:
        n, r = divmod(n - 1, 3)
        answer = "124"[r] + answer

    return answer


if __name__ == "__main__":
    print(solution(10))
