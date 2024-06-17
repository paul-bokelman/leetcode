# https://leetcode.com/problems/reverse-linked-list/?envType=study-plan-v2&envId=leetcode-75
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # iterative approach, place in list, reverse the list and build linked list
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        nodes = [head]
        current_node = head

        # get all the nodes in current order
        while current_node.next is not None:
            current_node = current_node.next
            nodes.append(current_node)

        # only 1 node -> return it
        if len(nodes) == 0:
            return head

        # reverse the list of nodes
        reversed_nodes = list(reversed(nodes))
        reversed_nodes[-1].next = None

        # rebuild chain
        new_head = current_new_node = reversed_nodes[0]
        reversed_nodes.pop(0)
        while len(reversed_nodes) > 0:
           current_new_node.next = reversed_nodes[0]
           current_new_node = current_new_node.next
           reversed_nodes.pop(0)

        return new_head
    
    # recursive approach
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return head