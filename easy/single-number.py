# https://leetcode.com/problems/single-number/?envType=study-plan-v2&envId=leetcode-75
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        collection = set() 

        for n in nums:
            if n not in collection:
                collection.add(n)
            else:
                collection.remove(n)

        return collection.pop()
    
print(Solution().singleNumber([2,2,1]))
print(Solution().singleNumber([4,1,2,1,2]))
print(Solution().singleNumber([1]))