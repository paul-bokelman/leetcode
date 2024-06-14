# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        return [True if k + extraCandies >= greatest else False for k in candies]
    
    # more efficient than list comprehension... probably because we just reassign values instead of copying them over
    def kidsWithCandies2(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        for i in range(len(candies)):
            if(candies[i] + extraCandies >= greatest):
                candies[i] = True
            else:
                candies[i] = False
        return candies
        
print(Solution().kidsWithCandies([2,3,5,1,3], 3))