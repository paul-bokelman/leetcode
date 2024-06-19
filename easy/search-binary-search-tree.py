# https://leetcode.com/problems/search-in-a-binary-search-tree/description/?envType=study-plan-v2&envId=leetcode-75
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # recursively search tree for value
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # root is None or value found -> return root and exit
        if not root or root.val == val: #/ combining this check improves efficiency by ~15ms
            return root
        
        # current root value is less than target -> continue right (getting bigger) 
        if root.val < val:
            return self.searchBST(root.right, val)
        # otherwise it's less than target -> continue left (getting smaller)
        else:
            return self.searchBST(root.left, val)