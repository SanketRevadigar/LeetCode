# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        
        def dfs(root,prevSum,targetSum):
            count = 0
            if not root:
                return 0
            
            curSum = prevSum + root.val                 #current sum is previous sum + present node's value
            if curSum - targetSum in rec:               #if this values is in rec then add the frequency of this value to count
                count += rec[curSum - targetSum]
            if curSum in rec:                           #if curSum in rec increment it else set to 1
                rec[curSum] += 1
            else:
                rec[curSum] = 1
            
            count += dfs(root.left,curSum,targetSum)   #as the fn returns count, add the value to count
            count += dfs(root.right,curSum,targetSum)
            rec[curSum] -= 1                           #set rec to -1 when the node goes to other side, as curSum not useful
            
            return count
        
        rec={0:1}                                       #Consider Target is 15. Now, 10 + 5 = 15. It is direct path from Root to One node. Now, curSum (15) - targetSum(15) = 0. This is valid result. Thus we have initiated rec as {0:1}.
        return dfs(root,0,targetSum)
    
    
    #Time Complexity -O(N)