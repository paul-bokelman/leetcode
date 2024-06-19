# https://leetcode.com/problems/min-cost-climbing-stairs/description/?envType=study-plan-v2&envId=leetcode-75
from typing import List

class Solution:
    def _find_optimal_step(self, current_index: int, cost: List[int]) -> tuple[int,int]:
        # check if most optimal step is actually the more expensive one


        one_step = current_index + 1
        two_step = current_index + 2

        if one_step == len(cost) or two_step >= len(cost):
            return (-1, 0)
        
        (new_index, lower_cost) = (one_step, cost[one_step]) if cost[one_step] < cost[two_step] else (two_step, cost[two_step])

        return (new_index, lower_cost)



    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = 0
        current_index = -1

        if len(cost) == 3:
            return cost[1]


        # each index -> find cheapest next index and 
        while current_index < len(cost) or current_index != -1:
            (new_index, lower_cost) = self._find_optimal_step(current_index, cost)

            if new_index == -1:
                print(f'exiting at {min_cost}')
            else:
                print(f'choosing ({new_index})={lower_cost}')

            if new_index == -1:
                break

            current_index = new_index    
            min_cost += cost[current_index]

        

        return min_cost

print(Solution().minCostClimbingStairs([10,15,20]))
print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))

