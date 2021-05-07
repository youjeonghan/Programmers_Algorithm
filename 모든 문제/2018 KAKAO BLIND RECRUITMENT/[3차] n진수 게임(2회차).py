# 2018 KAKAO BLIND RECRUITMENT      [3차] n진수 게임
def solution(n, t, m, p):
    li = ["0"] * ((t - 1) * m + p + 1)
    idx = 2
    num = 1
    dic = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    for i in range(0, 10):
        dic[i] = str(i)

    while idx != len(li):
        temp = num
        st = ""
        while temp != 0:
            temp, left = temp // n, temp % n
            st = dic[left] + st

        for ch in st:
            if idx != len(li):
                li[idx] = ch
                idx += 1
        num += 1

    result = [li[p + i * m] for i in range(t)]
    return "".join(result)


if __name__ == "__main__":
    print(solution(2, 4, 2, 1))
    print(solution(16, 16, 2, 1))
