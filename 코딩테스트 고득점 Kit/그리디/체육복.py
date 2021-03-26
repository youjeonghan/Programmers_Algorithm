# 1레벨     코딩테스트 고득점 Kit     체육복
def solution(n, lost, reserve):
    lost, reserve = list(set(lost) - set(reserve)), list(set(reserve) - set(lost))
    lost.sort()
    reserve.sort(reverse=True)
    n -= len(lost)
    for i in lost:
        while reserve and reserve[-1] < i - 1:
            reserve.pop()

        if not reserve:
            break

        if i - 1 <= reserve[-1] <= i + 1:
            n += 1
            reserve.pop()

        elif reserve[-1] > i + 1:
            continue

    return n


if __name__ == "__main__":
    print(solution(3, [3, 1, 2], [2, 4, 3]))  # 123 432
