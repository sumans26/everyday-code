# https://leetcode.com/problems/symmetric-tree/

# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def ismirrored(left, right):
    
    # print(left,right)
    # root_symm = False
    if(left == None and right == None):
        # print("True for", left, right)
        return True
    
    if (left != None and right != None):
        if(left.val == right.val) : 
            exterior_symm = ismirrored(left.left, right.right)
            interior_symm = ismirrored(left.right, right.left)
            ans = exterior_symm and interior_symm
            # print(ans, "for", left, right)
            return (ans)
    
    # print("False for", left, right)
    return False
        

class Solution(object):

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return ismirrored(root.left, root.right)
