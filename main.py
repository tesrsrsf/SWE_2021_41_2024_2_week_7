from typing import List

def twoSum(nums: List[int], target: int) -> List[int]: 
    for i in range(0, len(nums)):
        for j in range(0, len(nums)): 
            if i == j:
                continue
            if nums[i] + nums[j] == target: 
                return [i, j]


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
