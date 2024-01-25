#https://leetcode.com/problems/diameter-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def helperfn(root):
    if root == None:
        return 0,0
    
    left_depth, left_d = helperfn(root.left)

    right_depth, right_d = helperfn(root.right)

    return (max(left_depth, right_depth) + 1, max([left_d, right_d, 1+right_depth+left_depth]))


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth, d = helperfn(root)
        return d