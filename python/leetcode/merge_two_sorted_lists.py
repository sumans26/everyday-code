# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        sorted_list = None
        if(list1.val < list2.val):
            sorted_list = ListNode(list1.val)
        else:
            sorted_list = ListNode(list2.val)
        
        