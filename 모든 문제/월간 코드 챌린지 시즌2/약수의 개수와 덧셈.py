# 레벨1     월간 코드 챌린지 시즌2      약수의 개수와 덧셈


def solution(left, right):
    li = [i for i in range(left, right + 1)]
    return sum([i if get_divisor_len(i) % 2 == 0 else -i for i in li])


def get_divisor_len(num):
    temp_li = []
    for i in range(1, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            temp_li.append(i)
            if num != i ** 2:
                temp_li.append(num // i)
    return len(temp_li)


if __name__ == "__main__":
    print(solution(13, 17))
