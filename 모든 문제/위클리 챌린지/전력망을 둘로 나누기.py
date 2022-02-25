# 2레벨     위클리 챌린지       전력망을 둘로 나누기
# 다시 풀기 (해답보고품)
# 개선 가능

from collections import defaultdict, deque


def solution(n, wires):
    answer = float("inf")
    tree = defaultdict(list)
    for a, b in wires:
        tree[a].append(b)
        tree[b].append(a)

    for a, b in wires:
        tree[a].remove(b)
        tree[b].remove(a)
        cnt = bfs(n, tree, a)
        tree[a].append(b)
        tree[b].append(a)
        answer = min(answer, abs(n - 2 * cnt))
    return answer


def bfs(n, tree, start):
    visited = [0] * (n + 1)
    stack = deque([start])
    visited[start] = 1
    cnt = 1
    while stack:
        t = stack.popleft()
        for i in tree[t]:
            if visited[i] == 0:
                stack.append(i)
                visited[i] = 1
                cnt += 1
    return cnt


if __name__ == "__main__":
    print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
