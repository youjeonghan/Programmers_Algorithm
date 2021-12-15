# 레벨2     2021 Dev-Matching: 웹 백엔드 개발자(상반기)     행렬 테두리 회전하기


def solution(rows, columns, queries):
    arr = [[r * columns + c + 1 for c in range(columns)] for r in range(rows)]
    result = []
    for x1, y1, x2, y2 in queries:
        x, y = x1, y1
        tempList = []
        tempList.append(arr[x - 1][y - 1])
        before_temp = arr[x - 1][y - 1]
        for _ in range(y2 - y1):
            y += 1
            tempList.append(arr[x - 1][y - 1])
            temp = arr[x - 1][y - 1]
            arr[x - 1][y - 1] = before_temp
            before_temp = temp
        for _ in range(x2 - x1):
            x += 1
            tempList.append(arr[x - 1][y - 1])
            temp = arr[x - 1][y - 1]
            arr[x - 1][y - 1] = before_temp
            before_temp = temp
        for _ in range(y2 - y1):
            y -= 1
            tempList.append(arr[x - 1][y - 1])
            temp = arr[x - 1][y - 1]
            arr[x - 1][y - 1] = before_temp
            before_temp = temp
        for _ in range(x2 - x1):
            x -= 1
            tempList.append(arr[x - 1][y - 1])
            temp = arr[x - 1][y - 1]
            arr[x - 1][y - 1] = before_temp
            before_temp = temp
        result.append(min(tempList))

    return result


if __name__ == "__main__":
    print(solution(3, 3, [[1, 1, 3, 3]]))
