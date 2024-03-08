# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        s = str(self.val)    
        s += ("{" + str(self.left) + "}, ") 
        s += ("{" + str(self.right) + "}")
        return s

class Solution(object):

    def lhListToBST(self,nums, l, r):
        
        middle = (l+r)/2

        root = TreeNode(nums[middle])

        if(middle!=l):
            root.left = lhListToBST(nums,l,
        

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        self.lhListToBST(nums, 0, len(nums)-1)


        