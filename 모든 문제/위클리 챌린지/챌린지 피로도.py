# 레벨2     위클리 챌린지       피로도
# 다시 풀어야함
# 정답 보고 풀었음


def solution(k, dungeons):
    global result, visited
    result = 0
    visited = [0] * len(dungeons)
    dfs(k, 0, dungeons)
    return result


def dfs(k, cnt, dungeons):
    global result, visited
    for idx, i in enumerate(dungeons):
        if k < i[0]:
            result = max(result, cnt)
        elif visited[idx] == 0:
            visited[idx] = 1
            dfs(k - i[1], cnt + 1, dungeons)
            visited[idx] = 0


if __name__ == "__main__":
    print(solution(80, [[80, 20], [50, 40], [30, 10]]))
