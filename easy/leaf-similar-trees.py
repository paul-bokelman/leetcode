# https://leetcode.com/problems/leaf-similar-trees/?envType=study-plan-v2&envId=leetcode-75
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# approach: use depth first search to construct leaf arrays for each tree and compare
class Solution:
    def _dfs(self, root: TreeNode, leaves: list[int]):
        # no children -> add to leaves
        if root.left is None and root.right is None:
            leaves.append(root.val)
        
        # has left node -> add to stack for continuation
        if root.left is not None:
            self._dfs(root.left, leaves)

        # has right node -> add to stack for continuation
        if root.right is not None:
            self._dfs(root.right, leaves)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # if either tree is empty -> not similar
        if root1 is None or root2 is None:
            return False
        
        #/ sets are completely unordered, had to use list to maintain order of leaves
        root1_leaves = []
        root2_leaves = []

        # calculate all leaves for each root
        self._dfs(root1, root1_leaves)
        self._dfs(root2, root2_leaves)

        #/ faster comparison of values (as opposed to using a loop with zip)
        return root1_leaves == root2_leaves