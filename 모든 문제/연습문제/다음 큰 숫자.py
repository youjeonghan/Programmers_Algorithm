# 레벨2     연습 문제       다음 큰 숫자
# 다시 풀기


def solution(n):
    temp = list(format(n, "b"))
    # print("".join(temp))
    if temp[-1] == "1":
        for idx in range(len(temp) - 2, -1, -1):
            if idx == 0:
                temp[idx] = "10"
            elif temp[idx] == "0":
                temp[idx] = "1"
                temp[-1] = "0"
                break
    else:
        cnt = -1
        for idx in range(len(temp) - 2, -1, -1):
            if temp[idx] == "1":
                cnt += 1
            if idx == 0:
                temp[idx] = "10"
            elif temp[idx] == "0" and temp[idx + 1] == "1":
                temp[idx] = "1"
                for i in range(1, len(temp) - cnt - 1):
                    temp[idx + i] = "0"
                for j in range(0, cnt):
                    temp[idx + i + j] = "1"
                break
    # print("".join(temp))
    return int("".join(temp), 2)


if __name__ == "__main__":
    print(solution(5))
