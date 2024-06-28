# https://leetcode.com/problems/longest-increasing-subsequence/description/
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lengths = [1] * len(nums) # path length for each node (number) 

        # compute sub problems -> find longest sub problem -> add to lengths
        for i in range(1, len(lengths)):
            sub_problems = []

            # compute all sub problems
            for k in range(i):
                # if prev less than current -> add prev's length to sub problems
                if nums[k] < nums[i]:
                    sub_problems.append(lengths[k])

            # update lengths with longest length from sub problems
            lengths[i] = 1 + max(sub_problems, default=0)

        # get and return longest length
        return max(lengths, default=0)

print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
print(Solution().lengthOfLIS([0,1,0,3,2,3]))
print(Solution().lengthOfLIS([7,7,7,7,7,7,7]))