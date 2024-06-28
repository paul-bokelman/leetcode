# https://leetcode.com/problems/determine-if-two-strings-are-close/?envType=study-plan-v2&envId=leetcode-75
from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # different lengths -> can't be similar
        if len(word1) != len(word2):
            return False
        
        # count and sort frequencies
        count_w1 = Counter(word1)
        count_w2 = Counter(word2)

        # different frequencies -> not similar
        if sorted(list(count_w1.values())) != sorted(list(count_w2.values())):
            return False
        
        # contain different characters -> not similar (can't convert)
        if set(count_w1.keys()) != set(count_w2.keys()):
            return False
        
        return True
    
print(Solution().closeStrings("abc", "bca"))
print(Solution().closeStrings("a", "aa"))
print(Solution().closeStrings("cabbba", "abbccc"))
print(Solution().closeStrings("cabbba", "aabbss"))
print(Solution().closeStrings("uau", "ssx"))