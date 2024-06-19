# https://leetcode.com/problems/maximum-depth-of-binary-tree/?envType=study-plan-v2&envId=leetcode-75
from typing import Optional
from collections import deque
# from utils.tree import TreeNode, buildTree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# approach: use breadth first search and log number of layers -> return final count
class Solution:
    # alternative approach (leverage binary tree recursively)
    def maxDepthAlternative(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0 
        
        left_height=self.maxDepthAlternative(root.left) # 
        right_height=self.maxDepthAlternative(root.right)
        if left_height >= right_height:
            return left_height + 1
        else:
            return right_height + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # keep track of depth
        depth = 0

        # if there is no root we can't construct a tree
        if root is None:
            return 0

        # node queue that will be mutated as tree is constructed    
        queue = [root]

        # while there are still nodes to search -> search them
        while queue:
            layer_bound = len(queue) # check out many checks left in layer

            # each node in layer -> append valid children 
            for i in range(layer_bound):
                current_node = queue[i]

                # if left child -> add to queue
                if current_node.left is not None:
                    queue.append(current_node.left)
                
                # if right child -> add to queue
                if current_node.right is not None:
                    queue.append(current_node.right)
            
            queue = queue[layer_bound:] # 
            depth += 1 # 

        return depth