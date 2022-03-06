# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):                                      #recursive dfs function
            if not root:                                    #if no node, return True and the height
                return [True,0]                             #height is returned to basicalluy check the balance factor
            
            left = dfs(root.left)                           #run dfs on left and right nodes
            right = dfs(root.right)
            balanced = (left[0] and right[0] and            #storing True or False in this variable, if difference btn left & right
                        abs(left[1] - right[1]) <= 1)       #is <= 1 and checking if both left & right are True
            
            return [balanced, 1 + max(left[1], right[1])]   #return balance and increment the height by taking max of both
        
        return dfs(root)[0]                                 #call dfs and return only the balance parameter
      
        
        
        #Time - O(N) N-No of Nodes in tree