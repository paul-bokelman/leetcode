# https://leetcode.com/problems/guess-number-higher-or-lower/?envType=study-plan-v2&envId=leetcode-75

# use binary search approach
class Solution:
    pick = 6
    # provided guess api from leet code
    def guess(self, num: int) -> int:
        if num > self.pick:
            return -1
        if num < self.pick:
            return 1
        return 0
    def guessNumber(self, n: int, pick: int) -> int:
        self.pick = pick

        # check if upper bound is answer
        if self.guess(n) == 0:
            return n

        middle = n // 2
        lower_bound = 0 # use numbers instead of lists
        upper_bound = n

        while True:
            guess_result = self.guess(middle) # get result of guess
            # check if correct answer
            if guess_result == 0:
                break
            
            # current middle is higher than target
            if guess_result == -1:
                upper_bound = middle

            # current middle is lower than target
            if guess_result == 1:
                lower_bound = middle

            # get middle of upper and lower bound
            middle = (lower_bound + upper_bound) // 2

        return middle

print(Solution().guessNumber(10, 6))
print(Solution().guessNumber(2, 1))
print(Solution().guessNumber(1, 1))