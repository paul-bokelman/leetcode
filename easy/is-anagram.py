class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for c in s:
            if c in t:
                index = t.index(c)
                t_list = list(t)
                t_list.pop(index)
                t = "".join(t_list)
            else:
                return False

        return len(t) == 0

    
print(Solution().isAnagram("racecar", "carrace"))
print(Solution().isAnagram("jar", "jam"))