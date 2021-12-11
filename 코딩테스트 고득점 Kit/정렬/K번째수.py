# 레벨1     정렬      K번째수


def solution(array, commands):
    result = []
    for s, e, t in commands:
        temp = array[s - 1 : e]
        tmep = temp.sort()
        result.append(temp[t - 1])
    return result


if __name__ == "__main__":
    print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
