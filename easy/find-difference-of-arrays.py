# https://leetcode.com/problems/find-the-difference-of-two-arrays/?envType=study-plan-v2&envId=leetcode-75
from typing import List

# Approach: loop over nums1 and store intersection indexes, then remove intersections for each list
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # convert to set to remove duplicates
        n1_set = set(nums1)
        n2_set = set(nums2)

        intersections: List[int] = []
        for n1 in n1_set:
                # is intersection -> store in intersections
                if n1 in n2_set:
                    intersections.append(n1)


        return [[n for n in n1_set if n not in intersections], [n for n in n2_set if n not in intersections]]

    def findDifferenceSimplified(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # convert to sets
        n1 = set(nums1) 
        n2 = set(nums2)

        # return difference of sets
        return [list(n1 - n2), list(n2 - n1)]

    
print(Solution().findDifference([1,2,3], [2,4,6]))
print(Solution().findDifference([1,2,3,3], [1,1,2,2]))