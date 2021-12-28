# 레벨3     탐욕법(Greedy)      섬 연결하기
# 22분 소요
# MST 최소 신장 트리
# Kruskal 크루스칼 알고리즘
# Union-Find 유니온 파인드


def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(0, n)]

    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    def find(a):
        if a == parent[a]:
            return a
        parent[a] = find(parent[a])
        return parent[a]

    arr = []
    result = 0
    for i in costs:
        if find(i[0]) != find(i[1]):
            union(i[0], i[1])
            result += i[2]
    return result


if __name__ == "__main__":
    print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
