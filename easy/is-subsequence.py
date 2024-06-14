# https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    # recursively find relative index above lower_bound
    def _findProceedingIndex(self, lower_bound: int, char: str, t: str):
        try:
            relative_index = t.index(char)

            # mutate input string for future checks
            t_list = list(t)
            t_list[relative_index] = '0'
            t = "".join(t_list)

            # if index less than lower bound -> try again
            if relative_index <= lower_bound:
                return self._findProceedingIndex(lower_bound, char, t)
            
            return relative_index

        except:
            # character not found
            return -1

    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        indexes: list[int] = []

        # for each character in string 
        for c in s:
            # if character is in t -> keep index and replace letter for repeats
            lower_bound = indexes[-1] if len(indexes) > 0 else -1
            relative_index = self._findProceedingIndex(lower_bound, c, t)

            if relative_index != -1:
                indexes.append(relative_index)
        
        # if not all characters were found -> false
        if len(indexes) != len(s):
            return False

        # check if indexes are out of order
        for i in range(len(indexes)):
            if i == 0:
                continue
            # if previous index is larger -> out of order
            if indexes[i] < indexes[i - 1]:
                # if this fails and there are still remaining character -> recursively call 
                if s[0] in t:
                    return self.isSubsequence(s, t)
                print(indexes)
                return False

        return True
    def isSubsequenceSimple(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            # in t -> remove from t and continue
            if s[i] in t:
                t = t[t.index(s[i])+1:]
            # not found -> just exit with false
            else:
                return False
        return True



print(Solution().isSubsequence("ab", "baab"))
print(Solution().isSubsequence("axc", "ahbgdc"))