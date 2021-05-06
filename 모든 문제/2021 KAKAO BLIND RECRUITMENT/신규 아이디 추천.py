# 정규표현 연습하기 좋은 문제
import re


def solution(new_id):
    # 1단계
    parse = new_id.lower()

    # 2단계
    parse = re.compile(r"[a-z]+|[0-9]+|[.]+|[-]+|[_]+").findall(parse)

    # 3단계
    parse = re.compile(r"[a-z]+|[0-9]+|[.]+|[-]+|[_]+").findall("".join(parse))
    parse = ["." if i[0] == "." and len(i) > 1 else i for i in parse]

    # 4단계
    if parse and parse[0] == ".":
        del parse[0]
    if parse and parse[-1] == ".":
        del parse[-1]

    # 5단계
    if not parse:
        parse = ["a"]
    parse = "".join(parse)

    # 6단계
    parse = parse[:15]
    if parse and parse[-1] == ".":
        parse = parse[:-1]

    # 7단계
    while len(parse) < 3:
        parse += parse[-1]

    return parse


if __name__ == "__main__":
    # print(solution("z-+.^."))
    # print(solution("=.="))
    print(solution("b......@"))
