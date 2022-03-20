# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root,prevValue):
            if not root:
                return 
            if prevValue <= root.val:
                self.count += 1
            prevValue = max(prevValue,root.val)
            dfs(root.left,prevValue)
            dfs(root.right,prevValue)

        self.count=0
        dfs(root,root.val)
        return self.count
    
    #Time: O(N), where N is the number of nodes in the binary tree.
    #Space: O(H), where H is the height of binary tree.