# https://leetcode.com/problems/binary-search/description/
# https://en.wikipedia.org/wiki/Binary_search
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower_bound = 0 # lower search bound
        upper_bound = len(nums) - 1 # upper search bound

        # continue as long as lower bound is less than or equal to upper bound
        while lower_bound <= upper_bound:
            # get the current middle index (average floor of lower and upper)
            middle = (lower_bound + upper_bound) // 2

            # if the current index is the target -> return the index
            if nums[middle] == target:
                return middle

            # current element is less than the target -> get right side of array (excluding current)
            if nums[middle] < target:
                lower_bound = middle + 1
            # otherwise (element greater than target) -> get left side of array (excluding current)
            else:
                upper_bound = middle - 1
        return -1 # no element found


print(Solution().search([-1,0,3,5,9,12], 9))
print(Solution().search([-1,0,3,5,9,12], 2))