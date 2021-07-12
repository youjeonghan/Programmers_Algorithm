# 2018 KAKAO BLIND RECRUITMENT      [1차] 추석 트래픽
import re
from datetime import datetime, timedelta


def solution(lines):
    time_list = []
    for line in lines:
        date, time, runtime = re.split(r" ", line)
        e_time = datetime.strptime((time), "%H:%M:%S.%f")
        s_time = e_time - timedelta(seconds=float(runtime[:-1]), milliseconds=-1)
        time_list.append([s_time, e_time])

    time_list.sort(key=lambda x: x[1])

    result = 0
    for idx, target in enumerate(time_list):
        start = target[1]
        end = start + timedelta(seconds=1, milliseconds=-1)

        # last = end + timedelta(seconds=3)
        cnt = 0
        for i in range(idx, len(time_list)):
            if not time_list[i][1] < start and not end < time_list[i][0]:
                cnt += 1

        result = max(result, cnt)

    return result


if __name__ == "__main__":
    print(
        solution(
            [
                "2016-09-15 20:59:57.421 0.351s",
                "2016-09-15 20:59:58.233 1.181s",
                "2016-09-15 20:59:58.299 0.8s",
                "2016-09-15 20:59:58.688 1.041s",
                "2016-09-15 20:59:59.591 1.412s",
                "2016-09-15 21:00:00.464 1.466s",
                "2016-09-15 21:00:00.741 1.581s",
                "2016-09-15 21:00:00.748 2.31s",
                "2016-09-15 21:00:00.966 0.381s",
                "2016-09-15 21:00:02.066 2.62s",
            ]
        )
    )
    # print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:05.001 2s"]))
