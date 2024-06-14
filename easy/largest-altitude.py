# https://leetcode.com/problems/find-the-highest-altitude/description/?envType=study-plan-v2&envId=leetcode-75
from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # current and highest start at elevation 0
        current_height = highest = 0

        # for each net gain -> check if current elevation is higher, if so -> record
        for i in range(len(gain)):
            current_height += gain[i]
            if current_height > highest:
                highest = current_height

        return highest
    
print(Solution().largestAltitude([-5,1,5,0,-7]))