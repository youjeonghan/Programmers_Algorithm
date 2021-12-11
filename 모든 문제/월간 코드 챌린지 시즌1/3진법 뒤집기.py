# 레벨1     월간 코드 챌린지 시즌1      3진법 뒤집기


def solution(n):
    temp = ""
    while n:
        n, r = divmod(n, 3)
        temp = str(r) + temp

    result = 0
    for idx, v in enumerate(temp):
        result += int(v) * 3 ** (idx)

    return result


if __name__ == "__main__":
    print(solution(45))
