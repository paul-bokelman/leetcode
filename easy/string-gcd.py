# https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75

# "ABABAB" % AB && "ABAB" % AB = 0
# remainder must be zero 

# approach
# - find common pattern in small string and large string 

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # not divisible
        if str1 + str2 != str2 + str1:
            return ""

        candidates = []

        # get the smaller string to loop over
        (smaller_str, larger_string) = (str1, str2) if len(str1) < len(str2) else (str2, str1)

        # store temporary pattern chain
        chain = []

        # loop over string and find candidates
        for character in smaller_str:
            # add to current pattern chain
            chain.append(character)
            chain_str = "".join(chain)

            # if the pattern in larger string -> add it to candidates
            if chain_str in larger_string:
                candidates.append(chain_str)
            # otherwise clear chain
            else:
                chain = []

        # starting from the largest string -> check if str1 & str2 % = 0
        for candidate in reversed(candidates):
            # check if % str = 0 by replacing all occurrences of candidate in each string and checking if empty 
            if(len(larger_string.replace(candidate, "")) == 0 and len(smaller_str.replace(candidate, "")) == 0):
                return candidate

        return ""
    def gcdOfStrings2(self, str1: str, str2: str) -> str:
        # not divisible
        if str1 + str2 != str2 + str1:
            return ""

        # get the smaller string to loop over
        (smaller_str, larger_string) = (str1, str2) if len(str1) < len(str2) else (str2, str1)

        # store temporary pattern chain
        valid = []
        candidate = []

        # loop over string and find candidates
        for character in smaller_str:
            # add to current pattern candidate
            candidate.append(character)
            candidate_str = "".join(candidate)

            # if the pattern in larger string -> check if divisor
            if candidate_str in larger_string:
                # check if % str = 0 by replacing all occurrences of candidate in each string and checking if empty 
                if(len(larger_string.replace(candidate_str, "")) == 0 and len(smaller_str.replace(candidate_str, "")) == 0):
                    valid.append(candidate_str)
                    # return candidate_str
            # otherwise clear candidate
            else:
                candidate = []

        if(len(valid) > 0):
            return valid[-1]

        return ""
    # leet code submitted code
    def gcdOfStringsFaster(self, str1: str, str2: str) -> str:
        # not divisible
        if str1 + str2 != str2 + str1:
            return ""
        
        # gcd of 2 numbers using euclidean algorithm
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # find gcd of lengths of strings
        gcd_length = gcd(len(str1), len(str2))

        return str1[:gcd_length]
        


# print(Solution().gcdOfStrings("ABCABC", "ABC"))
# print(Solution().gcdOfStrings2("ABCABC", "ABC"))
print(Solution().gcdOfStringsFaster("ABCABC", "ABC"))
        