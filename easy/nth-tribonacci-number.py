# https://leetcode.com/problems/n-th-tribonacci-number/description/?envType=study-plan-v2&envId=leetcode-75
from collections import deque

class Solution:
    def tribonacci(self, n: int) -> int:
        # n is 0 -> just return 0 (nothing to calc)
        if n == 0:
            return 0
        
        current_n = 1 # track current iteration of sequence
        previous_quantities = deque([0,1,1]) # store last 3 calculated quantities in order

        current_sum = 1 # store sum

        # continue until tribonacci of n is calculated
        while current_n < n - 1:
            current_sum = sum(previous_quantities) # calculate sum of previous 3 values
            previous_quantities.popleft() # remove the oldest value
            previous_quantities.append(current_sum) # append the sum for next calculation
            current_n += 1 # iteration complete -> increment count

        return current_sum


print(Solution().tribonacci(4))
print(Solution().tribonacci(25))