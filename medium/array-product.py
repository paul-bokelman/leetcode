# https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=leetcode-75
# https://www.youtube.com/watch?v=p-ss2JNynmw
#todo: unfinished
from typing import List

# notes: 
# - multiplying numbers stores information
# - sliding window technique is O(n)

class Solution:
    # linear solution
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # always excluding 1 element in window (len - 1 consecutive elements )
        window_size = len(nums) - 1 
        products = [1 for _ in range(len(nums))]

        # calculate initial product

        for n in nums[1:]:
            products[0] *= n

        # shift window len(nums) times??
        # for i in range(len(nums)):



        return []
    # quadratic solution
    def productExceptSelfQuadratic(self, nums: List[int]) -> List[int]:
        products = [1 for _ in range(len(nums))]

        seen = set()
        for i in range(len(nums)):
            for j in range(len(products)):
                if i != j:
                    products[i] *= nums[j]
                    if (products[i], nums[j]) in seen:
                        print('duplicate', (products[i], nums[j]))
                    else:
                        print('adding', (products[i], nums[j]), products)
                        seen.add((products[i], nums[j]))

        return products
        

# print(Solution().productExceptSelfQuadratic([1,2,3,4]))
print(Solution().productExceptSelf([1,2,3,4]))
# print(Solution().productExceptSelf([-1,1,0,-3,3]))
# print(Solution().productExceptSelfDivision([1,2,3,4]))