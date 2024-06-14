from typing import List

# approach
# use hash table with custom recursive hash function for quick lookup and insertion
class Solution:    
    # uniquely hash anagrams (sort characters)
    def _hash(self, s: str):
        # sort str in alphabetical order
        key = "".join(sorted(s))
        return key

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: dict[str, List[str]] = {}

        for i in range(len(strs)):
            # hash string to get key
            key = self._hash(strs[i])

            group = groups.get(key, None)
            # if key doesn't exist -> create it
            if group is None:
                groups[key] = [strs[i]]
            # otherwise add to list 
            else:
                groups[key].append(strs[i])

        # get values and return 
        return [g for g in groups.values()]
        
print(Solution().groupAnagrams(["act","pots","tops","cat","stop","hat"]))
print(Solution().groupAnagrams(["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]))
print(Solution().groupAnagrams(["mod","mop","pip","tug","hop","dog","met","zoe","axe","mug","fdr","for","fro","fdr","pap","ray","lop","nth","old","eva","ell","mci","wee","ind","but","all","her","lew","ken","awl","law","rim","zit","did","yam","not","ref","lao","gab","sax","cup","new","job","new","del","gap","win","pot","lam","mgm","yup","hon","khz","sop","has","era","ark"]))