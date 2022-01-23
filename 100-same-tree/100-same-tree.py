# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:         #if both are null
            return True
        if not p or not q:          #If 1 is null
            return False
        if p.val!=q.val:            #compare both values
            return False
        
        return (self.isSameTree(p.left,q.left)) and (self.isSameTree(p.right,q.right))
 
#Time complexity : O(N), where N is a number of nodes in the tree, since one visits each node exactly once.

#Space complexity : O(log⁡(N) in the best case of completely balanced tree and O(N) in the worst case of completely unbalanced tree, to keep a recursion stack. 