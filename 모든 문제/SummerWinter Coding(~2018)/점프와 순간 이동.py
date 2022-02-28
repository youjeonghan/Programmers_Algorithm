# 레벨2     Summer/Winter Coding(~2018)     점프와 순간 이동
# 9분 40초 소요


def solution(n):
    cnt = 0
    while n:
        n, t = divmod(n, 2)
        if t == 1:
            cnt += 1
    return cnt


if __name__ == "__main__":
    print(solution(5000))
