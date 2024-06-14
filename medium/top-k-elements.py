# https://neetcode.io/problems/top-k-elements-in-list
from typing import List

# approach: loop over each number in nums and stores it's number of occurrences in a hash table with. After all numbers have been checked, sort by descending order and get first k entries

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies: dict[int, int] = {}

        # for each number -> append it's frequency in hash table
        for n in nums:
            occurrence = frequencies.get(n, None)
            if occurrence is None:
                frequencies[n] = 0
            frequencies[n] = frequencies[n] + 1
        
        # sort frequencies to grab k most common
        sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

        # return keys with correct value
        return [n[0] for n in sorted_frequencies[:k]]
    
print(Solution().topKFrequent([1,2,2,3,3,3], 2))
print(Solution().topKFrequent([7,7], 1))