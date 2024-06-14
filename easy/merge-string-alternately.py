# https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75

# note: using array instead of string was much more efficient

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        # get the max length
        max_length = len(word1) if len(word1) > len(word2) else len(word2)
        # iterate to length of longer list
        for i in range(0, max_length):
            # if letter is accessible we append to list
            if(i < len(word1)):
                merged.append(word1[i])
            if(i < len(word2)):
                merged.append(word2[i])
            
        return "".join(merged)

solution = Solution()
print(solution.mergeAlternately("abc", "pqr"))
        