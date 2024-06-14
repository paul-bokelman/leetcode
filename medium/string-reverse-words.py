# https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def reverseWords(self, s: str) -> str:
        # extract words from string
        words = s.split(' ')
        # reverse and join words with spaces
        return " ".join(list(reversed(words)))
    def reverseWordsLessReadable(self, s: str) -> str:
        # remove spaces, reverse, and join
        # split removes spaces, and [::-1] reverses items
        return " ".join(s.split()[::-1])
    def reverseWordsManual(self, s: str) -> str:
        words = []

        previously_added = False
        for i in range(len(s)):
            if s[i] != ' ':
                if previously_added:
                    words[-1] += s[i]
                else:
                    previously_added = True
                    words.append(s[i])
            else:
                previously_added = False

        reversed_words = []
        for i in range(len(words), 0, -1):
            reversed_words.append(words[i - 1])
        
        constructed_string = ""

        for i in range(len(reversed_words)):
            if i == len(reversed_words) - 1:
                constructed_string += reversed_words[i]
            else:
                constructed_string += reversed_words[i]
                constructed_string += " "

        return constructed_string


# print(Solution().reverseWords("the sky is blue"))
# print(Solution().reverseWords("  hello world  "))
# print(Solution().reverseWords("a good   example"))
# print(Solution().reverseWords("  Bob    Loves  Alice   "))
print(Solution().reverseWordsManual("  Bob    Loves  Alice   "))
# print(Solution().reverseWordsLessReadable("  Bob    Loves  Alice   "))