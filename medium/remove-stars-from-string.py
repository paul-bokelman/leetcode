# https://leetcode.com/problems/removing-stars-from-a-string/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    # stack approach
    def removeStars(self, s: str) -> str:
        stack = [] # LiFo 

        for c in s:
            # regular character -> add to top of stack
            if c != "*":
                stack.append(c)
                continue
            
            # is star -> remove top character from stack and don't append star
            stack.pop()

        # return stack
        return "".join(stack)

    # continual approach
    def removeStarsContinual(self, s: str) -> str:
        s_list = list(s)
        current_index = 0
        last_character_index = -1

        # continue until all stars are removed 
        while "*" in s_list:
            
            # is star -> remove star and closest character
            if s_list[current_index] == "*":
                s_list.pop(current_index) # remove star
                current_index = current_index - 1

                # if star is not at index 0 -> remove character
                if last_character_index != -1:
                    s_list.pop(last_character_index)
                    current_index = current_index - 1
                
                # restart search
                last_character_index = -1

            # increment position
            last_character_index = current_index
            current_index += 1

        return "".join(s_list)


print(Solution().removeStars("leet**cod*e"))
print(Solution().removeStars("erase*****"))