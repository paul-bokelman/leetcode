from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# build referenced tree
def buildTree(tree: list[Optional[int]]) -> TreeNode | None: 
    # if there is no root we can't construct a tree
    if len(tree) == 0:
        return None

    # node queue that will be mutated as tree is constructed    
    node_queue = deque(tree)

    # initialize the root of the tree
    root_value = node_queue.popleft()
    assert root_value is not None, "No root value, can't build tree"
    current_node = TreeNode(root_value, None, None)

    # current level of tree
    depth = 1

    # number of children left to traverse at current level 2^depth
    children = 2

    # current parent
    current_parent = current_node

    # iteratively build tree
    while len(tree) > 0:
        # 
        return 