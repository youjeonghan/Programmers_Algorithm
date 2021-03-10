def solution(nums):
    answer = 0
    pick = int(len(nums) / 2)
    nums = list(set(nums))
    return min(len(nums), pick)


nums = [3, 1, 2, 3]
print(solution(nums))
