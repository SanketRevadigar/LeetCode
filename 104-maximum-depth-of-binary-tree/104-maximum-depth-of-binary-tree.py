# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        '''
        #Recursive DFS
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
        '''
        
        '''
        #Iterative DFS
        stack = [[root,1]]
        res=0
        while stack != []:
            node,depth=stack.pop()
            if node:
                res = max(res,depth)
                stack.append([node.left,depth+1])
                stack.append([node.right,depth+1])
        return res
        '''
        
        #Iterrative BFS
        if not root:
            return 0
        res = 0
        q = deque()
        q.append((root,1))
        while q:
            node,depth = q.popleft()
            if node:
                res = max(res,depth)
                q.append([node.left,depth+1])
                q.append([node.right,depth+1])
        return res
        
        
        
        #DFS-uses stack to pop, BFS uses queue to popleft
        
        #Time - O(N)
        #Space - O(N) Height of tree