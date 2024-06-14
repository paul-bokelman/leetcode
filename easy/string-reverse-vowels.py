# https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75

# approach
# 1. extract vowels list and relative index
# 2. reverse vowels list
# 3. replace indices 

class Solution:
    def reverseVowels(self, s: str) -> str:
        reversed_vowels = list(s)
        vowels_chars = {'a','e','i','o','u','A','E','I','O','U'}
        indexes = []
        vowels = []

        # extract vowels list and their relative indexes
        for i in range(len(reversed_vowels)):
            if reversed_vowels[i] in vowels_chars:
                vowels.append(reversed_vowels[i])
                indexes.append(i)
        
        # reverse vowels and place back into string with indexes
        for (i, v) in zip(indexes, reversed(vowels)):
            if v == '': 
                continue
            reversed_vowels[i] = v

        return "".join(reversed_vowels)
    
print(Solution().reverseVowels("leetcode"))
print(Solution().reverseVowels("hello"))


