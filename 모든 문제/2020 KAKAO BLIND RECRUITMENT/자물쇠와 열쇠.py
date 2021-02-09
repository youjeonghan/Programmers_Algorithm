# 2020 KAKAO BLIND RECRUITMENT      자물쇠와 열쇠
# key, lock이 정사각형인걸 중간에 인지함 (rotate 함수 더 간단히 가능할듯 노상관이긴함)
# 2차원 배열을 1차원배열로 변환 사용    /   answer = sum(my_list, [])
# 위 위짜르기 / 오른 돌리기-아래짜르기 / 아래 아래짜르기 / 왼 돌리기-위짜르기


def solution(key, lock):
    edge = len(key)
    hole = find_holl(lock, edge)

    # key = rotate(key)
    for i in range(0, edge):  # 위, 아래 이동키 확인
        for j in range(0, edge):
            temp = key[:]  # key 얕은복사
            for _ in range(i):
                del temp[0]
                temp.append([0 for _ in range(edge)])

            temp_r = temp_l = rotate(temp)
            for _ in range(j):
                del temp_l[0]
                temp_l.append([0 for _ in range(edge)])

            if check(temp_l, lock, edge, hole) == True:
                return True

            for _ in range(j):
                del temp_r[-1]
                temp_r.insert(0, [0 for _ in range(edge)])

            if check(temp_r, lock, edge, hole) == True:
                return True

            temp = key[:]  # key 얕은복사
            for _ in range(i):
                del temp[-1]
                temp.insert(0, [0 for _ in range(edge)])

            temp_r = temp_l = rotate(temp)
            for _ in range(j):
                del temp_l[0]
                temp_l.append([0 for _ in range(edge)])

            if check(temp_l, lock, edge, hole) == True:
                return True

            for _ in range(j):
                del temp_r[-1]
                temp_r.insert(0, [0 for _ in range(edge)])

            if check(temp_r, lock, edge, hole) == True:
                return True
    return False


def rotate(key):
    """ 90도 시계 방향 회전 """
    w = len(key[0])
    h = len(key)
    idx = 0

    temp = [[0 for _ in range(h)] for _ in range(w)]
    for i in range(w):
        for j in range(h - 1, -1, -1):
            temp[idx // h][idx % h] = key[j][i]
            idx += 1

    return temp


def find_holl(lock, edge):
    """ 리스트안에 lock의 홈이 좌표(튜플)가 담김 """
    temp = []
    for i in range(edge):
        for j in range(edge):
            if lock[i][j] == 0:
                temp.append((i, j))

    return temp


def check(key, lock, edge, hole):
    """ key와 lock이 맞는지 체크 """
    if edge ** 2 == sum(sum(key, [])) + sum(sum(lock, [])):
        for p in hole:
            if lock[p[0]][p[1]] == key[p[0]][p[1]]:
                return False
    else:
        return False

    return True


"""
입출력 예시
"""
key = [
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 1],
]
lock = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1],
]
# 답 true

print(solution(key, lock))


# print(rotate(key))