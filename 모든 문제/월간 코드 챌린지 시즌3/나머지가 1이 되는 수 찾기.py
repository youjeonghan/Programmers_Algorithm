# 레벨1     월간 코드 챌린지 시즌3      나머지가 1이 되는 수 찾기


def solution(n):
    num = 2
    while 1:
        if n % num == 1:
            return num
        num += 1


if __name__ == "__main__":
    print(solution(10))
