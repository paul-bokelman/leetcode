# https://neetcode.io/problems/string-encode-and-decode
from typing import List

class Solution:
    schema = ">"
    def encode(self, strs: List[str]) -> str:
        encoded = ""

        # apply schema before each word
        for s in strs:
            encoded += f'{self.schema}{s}'

        return encoded
    
    def decode(self, s: str) -> List[str]:
        strs = []

        # split string and schema
        i = -1
        for c in s:
            if c in self.schema:
                if c == ">":
                    i += 1
                strs.append("")
                continue
            strs[i] += c

        return strs
    

print(Solution().decode(Solution().encode(["neet","code","love","you"])))
print(Solution().decode(Solution().encode([""])))
print(Solution().decode(Solution().encode([])))
print(Solution().decode(Solution().encode(["","   ","!@#$%^&*()_+","LongStringWithNoSpaces","Another, String With, Commas"])))