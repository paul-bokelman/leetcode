# https://leetcode.com/problems/pascals-triangle/
from typing import List

class Solution:
    calculated_factorials = {
        0: 1,
        1: 1,
    }

    calculated_nCk = {}

    # calculate and memoize factorials
    def factorial(self, n) -> int:
        if n in self.calculated_factorials:
            return self.calculated_factorials[n]
        
        product = n * self.factorial(n - 1)
        self.calculated_factorials[n] = product

        return product
    
    # n choose k
    def nCk(self, n, k):
        if (n, k) in self.calculated_nCk:
            return self.calculated_nCk[(n,k)]

        computed = self.factorial(n) // (self.factorial(k) * self.factorial(n - k))
        self.calculated_nCk[(n,k)] = computed
        return computed

    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[]]

        for current_row in range(numRows):
            for current_col in range(current_row + 1):
                 triangle[current_row].append(self.nCk(current_row, current_col))
            if current_row + 1 != numRows:
                triangle.append([])

        return triangle
    
print(Solution().generate(5))
print(Solution().generate(1))