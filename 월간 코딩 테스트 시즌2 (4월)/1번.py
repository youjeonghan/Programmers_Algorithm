def solution(absolutes, signs):
    answer = 0
    for num, b in zip(absolutes, signs):
        if b == True:
            answer += num
        else:
            answer -= num
    return answer