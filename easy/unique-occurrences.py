# https://leetcode.com/problems/unique-number-of-occurrences/?envType=study-plan-v2&envId=leetcode-75
from typing import List
from collections import Counter

# calculate number of occurrences then ensure that # of unique elements matches # of unique occurrences (dictionary)
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = {}

        # number of occurrences of each unique element
        for n in arr:
            occurrence = occurrences.get(n, None)
            if occurrence is None:
                occurrences[n] = 0
            occurrences[n] += 1
            
        # check if any values are the same with set
        return len(set(occurrences.values())) == len(occurrences.values())
    # same implementation but with counter
    def uniqueOccurrencesCounter(self, arr: List[int]) -> bool:
        occurrences = Counter(arr) #/ counts number of unique occurrences and places in hashmap (exact same as above but abstracted)
        return len(set(occurrences.values())) == len(occurrences.values())

print(Solution().uniqueOccurrences([1,2,2,1,1,3]))
print(Solution().uniqueOccurrences([1,2]))
print(Solution().uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))
        