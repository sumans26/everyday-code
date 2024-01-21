# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
# Definition for a binary tree node.

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if(p.val > q.val) : p,q = q,p #making sure p < q
        if(root.val == p.val): return p
        elif(root.val == q.val): return q

        elif(p.val < root.val and q.val > root.val):
            return root
        else:
            if(p.val < root.val):
                return self.lowestCommonAncestor(root.left, p,q)
            else:
                return self.lowestCommonAncestor(root.right, p,q)
        