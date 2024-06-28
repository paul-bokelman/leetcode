# https://leetcode.com/problems/fibonacci-number/
from collections import deque

class Solution:
    # dp iterative solution
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        current_n = 3
        previous = deque([1, 1])

        while current_n != n:
            nth = previous[0] + previous[1]
            previous.append(nth)
            previous.popleft()
            current_n += 1

        return previous[0] + previous[1]
    

print(Solution().fib(2))
print(Solution().fib(3))
print(Solution().fib(4))