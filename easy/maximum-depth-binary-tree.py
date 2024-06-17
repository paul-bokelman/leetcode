# https://leetcode.com/problems/maximum-depth-of-binary-tree/?envType=study-plan-v2&envId=leetcode-75
from typing import Optional
from collections import deque
from utils.tree import TreeNode, buildTree

# approach: use breadth first search and log number of layers -> return final count
class Solution:
    def _bfs(self, root: Optional[TreeNode]):
        if root is None:
            return root
        

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])

        print(queue[0])


        return 0
    

    

print(Solution().maxDepth(buildTree([3,9,20,None,None,15,7])))