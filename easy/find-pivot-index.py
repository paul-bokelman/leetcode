# https://leetcode.com/problems/find-pivot-index/description/?envType=study-plan-v2&envId=leetcode-75
from typing import List

class Solution:
    # Quadratic solution
    def pivotIndexQuadratic(self, nums: List[int]) -> int:
        # for each index -> calculate and compare right and left sum
        for i in range(len(nums)):
            left = nums[:i] # left side of list 
            right = nums[i+1:] # right side of list excluding nums[i]

            if sum(left) == sum(right): # if equal -> index is pivot index
                return i

        return -1 # no pivot index

    #/ approach focuses on convergence to pivot index where you essentially have 2 lists being checked for an intersection
    #/ of course there are no lists but the idea is similar
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)

        for i in range(len(nums)):
            # add previous value to left sum
            if i > 0:
                left_sum += nums[i - 1]
            
            # subtract current value from right sum
            right_sum = right_sum - nums[i]

            # if left == right -> i is pivot index
            if left_sum == right_sum:
                return i

        return -1
    

print(Solution().pivotIndex([1,7,3,6,5,6]))
print(Solution().pivotIndex([1,2,3]))
print(Solution().pivotIndex([2,1,-1]))
