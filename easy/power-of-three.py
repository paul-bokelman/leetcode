# https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # initial checks (not divisible by 3 or less than 0)
        if n == 1:
            return True

        if n % 3 != 0 or n < 0:
            return False

        quotient = n # store current quotient

        # repeatedly divide by 3 until can't be evenly divided by 3
        while quotient > 1 and quotient % 3 == 0: 
            quotient = quotient // 3

        return quotient == 1
    
print(Solution().isPowerOfThree(27))
print(Solution().isPowerOfThree(0))
print(Solution().isPowerOfThree(-1))
print(Solution().isPowerOfThree(1))