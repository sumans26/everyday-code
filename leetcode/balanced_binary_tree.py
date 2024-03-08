#https://leetcode.com/problems/balanced-binary-tree/description/
from pydantic import Optional
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        :type root: TreeNode
        :rtype: bool
        """
    def helper_fn(self, root) : #returns height and bool
        
        if(root == None) : return 0, True

        lh, lb = self.helper_fn(root.left)
        if(not lb) : return -1, False
        
        rh, rb = self.helper_fn(root.right)
        if(not rb) : return -1, False

        if(abs(lh - rh) < 2) : 
            return max(lh, rh) + 1, True
        else:
            return -1, False

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.helper_fn (root)
