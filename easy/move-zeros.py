# https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75
from typing import List

class Solution:
     # doesn't maintain relative order of nums
    def moveZeroes(self, nums: List[int]) -> None:
        zeros_found = 0
        i = 0 
        # for each zero -> pop and append to back
        while i < len(nums):
            if len(nums) - zeros_found == i:
                return 
            # if a zero is found -> remove it and add it to end
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                zeros_found += 1
            else:
                i += 1


    # doesn't maintain relative order of nums
    def moveZeroesUnordered(self, nums: List[int]) -> None:
        # get all indexes of zeros
        zero_indexes = []
        for (i, n) in enumerate(nums):
            if n == 0:
                zero_indexes.append(i)
        
        # iterate backwards nums while swapping indexes
        for (i, zi) in zip(range(len(nums),0, -1), zero_indexes):
            nums[zi] = nums[i - 1]
            nums[i - 1] = 0


nums = [0,1,0,3,12]
Solution().moveZeroes(nums)
print(nums)
  