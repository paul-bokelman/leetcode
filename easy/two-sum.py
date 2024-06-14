# https://neetcode.io/problems/two-integer-sum
from typing import List

class Solution:
    # O(n) solution (utilizes constant hashmap operations)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap to record values seen as keys and their indexes as values
        seen = {} #/ hashmap has O(1) lookup and insertion
        for i in range(len(nums)):
            # if difference of target and value is present in hashmap -> get it's value
            seen_value = seen.get(target - nums[i], None)
            # if the value is present and isn't the same as nums[i] -> return [min, max]
            if seen_value is not None and seen_value != i:
                # return smallest first 
                return [min(i, seen[target - nums[i]]), max(i, seen[target - nums[i]])]
            
            # for each entry -> set key to it's value and it's value as it's index
            seen[nums[i]] = i
        return []
    # O(n^2) solution (checks all permutations)
    def twoSumQuadratic(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                # if sum of 2 numbers is target -> found solution
                if nums[i] + nums[j] == target:
                    # place smaller index first
                    return [min(i, j), max(i, j)]
        return []
        

print(Solution().twoSum([3,4,5,6], 7))
print(Solution().twoSum([5, 5], 10))
# print(Solution().twoSumQuadratic([3,4,5,6], 7))