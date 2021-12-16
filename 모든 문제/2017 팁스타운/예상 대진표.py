# 레벨2     2017 팁스타운       예상 대진표
# 35분 소요
# a, b min max 동시에 안해서 a,b 가 b, b 가 되버려서 오답이었음 뇌절
# 더 깔끔한 코드 존재


def solution(n, a, b):
    t = 1
    cnt = 0
    a, b = min(a, b), max(a, b)

    while t * 2 <= n:
        t *= 2
        cnt += 1
        if t == 2 and t >= b:
            return 1
        elif t >= b:
            a, b = a - t // 2, b - t // 2
            t = 1
            cnt = 0

        elif t >= a:
            while 1:
                t *= 2
                cnt += 1
                if t >= b:
                    return cnt


if __name__ == "__main__":
    print(solution(8, 4, 5))
