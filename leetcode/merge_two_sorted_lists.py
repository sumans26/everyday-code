# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        print(f"{self.val}, {self.next.print()}")


class Solution(object):
    def mergeTwoLists_recursive(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        sorted_list = None

        if (list1 == None):
            return list2
        elif (list2 == None):
            return list1
        else:
            sorted_list = ListNode(list1.val, self.mergeTwoLists(list1.next, list2)) if (
                list1.val < list2.val) else ListNode(list2.val, self.mergeTwoLists(list1, list2.next))
        return sorted_list
    
