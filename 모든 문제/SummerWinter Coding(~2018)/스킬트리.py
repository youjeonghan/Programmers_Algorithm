# 레벨2     Summer/Winter Coding(~2018)     스킬트리

from collections import defaultdict


def solution(skill, skill_trees):
    dic = defaultdict(lambda: -1)
    for i in range(len(skill)):
        dic[skill[i]] = i

    result = len(skill_trees)
    for i in skill_trees:
        cnt = 0
        for j in i:
            if dic[j] >= 0 and cnt != dic[j]:
                result -= 1
                break
            elif cnt == dic[j]:
                cnt += 1
    return result


if __name__ == "__main__":
    print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
