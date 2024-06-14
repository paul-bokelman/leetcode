# https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75
from typing import List

# uses sliding door technique
# sliding door is useful for computing values for sub-arrays (https://gist.github.com/syphh/6efc029460699ecad9231438a3668588)
class Solution:
    # compute average for array 
    def _compute_average(self, values: List[int]):
        average = 0.0
        for v in values:
            average += v

        return average / len(values)
    
    # use average and minimally compute new average
    def _recompute_average(self, k: int, current_average: float, old: int, new: int):
        return ((current_average * k) - old + new) / k
    
    # approach 1: compute average and use sliding window to find max average
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) < k:
            return 0
        current_average = self._compute_average(nums[:k])
        max_average = current_average

        for i in range(len(nums) - k):
            current_average = self._recompute_average(k, current_average, nums[i], nums[i+k])
            max_average = max(max_average, current_average)

        return max_average
    
    # approach 2: find max sum with sliding window then compute average (remove redundant calculations)
    def findMaxAverageEfficient(self, nums: List[int], k: int) -> float:
        # calculate sum for first k elements
        current_sum = max_sum = sum(nums[:k]) #/ more efficient than defining both 
        # for the remaining elements ahead of k -> compute and compare sum
        for i in range(len(nums) - k):
            # get current sum by "shifting" to the right -> remove last and add next
            current_sum = current_sum - nums[i] + nums[i+k] # adding by k because window is k length
            # if the computed sum is larger than current largest -> make largest
            if current_sum > max_sum: #/ comparison is more efficient than using max()
                max_sum = current_sum

        # get average
        return max_sum / k
    

# print(Solution().findMaxAverage([1,12,-5,-6,50,3], 4))
print(Solution().findMaxAverageEfficient([1,12,-5,-6,50,3], 4))