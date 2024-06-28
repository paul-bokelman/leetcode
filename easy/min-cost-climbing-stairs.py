# https://leetcode.com/problems/min-cost-climbing-stairs/description/?envType=study-plan-v2&envId=leetcode-75
from typing import List
# goal: find min cost to reach the end
# rules: end is out of list, start at i = 0 or 1, once paided -> can move 1-2 spots
# solve recursively -> memoize computations

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:        
        current_index = 0
        computed = []
        while current_index < len(cost):
            pass
        return 0

print(Solution().minCostClimbingStairs([10,15,20]))
print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
print(Solution().minCostClimbingStairs([0,1,2,2]))
print(Solution().minCostClimbingStairs([0,0,1,1]))


