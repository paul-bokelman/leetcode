# https://neetcode.io/problems/duplicate-integer
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        # for each number -> check if we've seen with hashmap O(1) lookup
        for (i, n) in enumerate(nums):
            if seen.get(n) is not None:
                return True
            seen[n] = i
        return False
         
print(Solution().hasDuplicate([1, 2, 3, 3]))