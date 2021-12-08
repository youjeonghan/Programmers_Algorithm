# 레벨1     월간 코드 챌린지 시즌2      음양 더하기


def solution(absolutes, signs):
    return sum(map(lambda x: x[0] if x[1] else -x[0], zip(absolutes, signs)))


if __name__ == "__main__":
    print(solution([4, 7, 12], [True, False, True]))
