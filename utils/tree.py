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
    node_queue = deque[int | None](tree)

    # initialize the root of the tree
    root_value = node_queue.popleft()
    assert root_value is not None, "No root value, can't build tree"

    # current level of tree
    depth = 1

    # current parent
    parents = deque[TreeNode | None]([TreeNode(root_value, None, None)])
    parent = parents[0] # current parent to assign left and right nodes to 
    
    iteration = 0 # current iteration; used to determine left or right placement and current index

    # iteratively build tree, go until all entries have been checked
    while len(node_queue) > 0:
        children = 2**depth # number of children left to traverse at current level 2^depth

        while children != 0 and len(node_queue) > 0: # iterate until current batch of children is finished
            assert parent is not None, "Parent is none"

            children -= 1
            child_value = node_queue.popleft()

            # if child is none -> just move on
            if child_value is None:
                if iteration % 2 == 0:
                    # get next parent
                    parent = parents[iteration]
                continue
    
            iteration += 1 # increment iteration (index of parent)

            child = TreeNode(child_value, None, None)

            # place right node and move to next non-None parent
            if iteration % 2 == 0:
                parent.right = child
                parent = parents[iteration - 1]

            # place left node
            else:
                parent.left = child

            parents.append(child)

        depth += 1
    
    return parents[0]





