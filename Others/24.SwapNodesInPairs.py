"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem 
without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = None if head == None else head.next
        
        # There are more than one nodes in the linkedlist.
        if head and newHead:
            temp = newHead.next
            newHead.next = head
            
            head.next = self.swapPairs(temp)
            return newHead
        else:
            return head
        
"""
Runtime: 24 ms, faster than 33.51% of Python online submissions for Swap Nodes in Pairs.
Memory Usage: 13.3 MB, less than 97.60% of Python online submissions for Swap Nodes in Pairs.
"""