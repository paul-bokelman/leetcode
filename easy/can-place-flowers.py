from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        placements = 0
        for i in range(len(flowerbed)):
            if placements == n:
                return True
            # get left and right positions
            left = flowerbed[i - 1] if i != 0 else 0
            right = flowerbed[i + 1] if i + 1 < len(flowerbed) else 0
            
            # check if left and right spots are empty, if so increment placements
            if left == 0 and right == 0 and flowerbed[i] != 1:
                flowerbed[i] = 1
                placements += 1

        if placements == n:
            return True
        return False

print(Solution().canPlaceFlowers([1,0,0,0,1,0,0], 2))
print(Solution().canPlaceFlowers([0,0,1,0,0], 1))
