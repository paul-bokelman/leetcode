# https://leetcode.com/problems/asteroid-collision/?envType=study-plan-v2&envId=leetcode-75
from typing import List

# approach: until previous and next states are equal -> get possible collisions, simulate each collision
# iteratively check and execute collisions
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i = 0 
        while len(asteroids) != 0:
            # on last element with no changes -> collisions are complete
            if i + 1 >= len(asteroids): 
                break
            
            # adjacent asteroids
            left, right = asteroids[i], asteroids[i+1]

            # not colliding -> move to next index
            if (left * right) > 0 or (left < 0 and right > 0):
                i += 1
                continue

            # same size -> destroy both
            if abs(left) == abs(right):
                asteroids.pop(i) # remove left
                asteroids.pop(i) # remove right (just i because indexes shift)
            # left is bigger -> remove right, right is bigger -> remove left 
            else:
                asteroids.pop(i+1 if abs(left) > abs(right) else i)
            
            # reset index (could just backtrack for greater efficiency)
            i = i - 1 if i > 0 else i
        
        return asteroids
    
print(Solution().asteroidCollision([5, 10, -5]))
print(Solution().asteroidCollision([8, -8]))
print(Solution().asteroidCollision([10, 2, -5]))
print(Solution().asteroidCollision([-1,12,6,6,-2,4,1,-3,2,2,5,-6,4])) # [-1,12,6,4]
print(Solution().asteroidCollision([-2,-1,1,2])) # [-2,-1,1,2]
