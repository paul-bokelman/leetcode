# https://leetcode.com/problems/climbing-stairs/

class Solution:
    calculated_factorials = {
        0: 1,
        1: 1,
    }
    # calculate and memoize factorials
    def factorial(self, n) -> int:
        if n in self.calculated_factorials:
            return self.calculated_factorials[n]
        
        product = n * self.factorial(n - 1)
        self.calculated_factorials[n] = product

        return product

    def climbStairs(self, n: int) -> int:
        combinations = { 0: 1 } # combination counts (key = # of 2's, value = permutations) 
        max_twos = n // 2 # total amount of times 2 can be in n

        # continue until all permutations are calculated
        while max_twos != 0:
            positions = n - (max_twos * 2) + max_twos # calculate available positions
            n_choose_k = self.factorial(positions) // (self.factorial(max_twos) * self.factorial(positions - max_twos)) # calculate combinations
            combinations[max_twos] = n_choose_k # add to combinations

            max_twos -= 1 # permutations complete -> move to next

        return sum(combinations.values())
    

print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
print(Solution().climbStairs(5))