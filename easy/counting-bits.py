# https://leetcode.com/problems/counting-bits/?envType=study-plan-v2&envId=leetcode-75
from typing import List

class Solution:
    # dynamic approach
    def countBitsDynamic(self, n: int) -> List[int]:
        # DP array initialization
        dp = [0] * (n + 1)

        dp[0] = 0 # no bits at index 0

        for i in range(1, n+1):
            print(i, i>>1,dp[i>>1], (i & 1))
            dp[i] = dp[i>>1] + (i & 1)

        return dp
    def countBits(self, n: int) -> List[int]:
        bits = []

        # for each number -> get binary and count 1s
        for i in range(0, n + 1):
            b = bin(i).replace('0b', '').replace('0', '') # remove prefix and all zeros
            bits.append(len(b)) # get the length of ones remaining

        return bits


# print(Solution().countBits(2))
# print(Solution().countBits(5))
print(Solution().countBitsDynamic(2))
print(Solution().countBitsDynamic(5))
        