# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])
        
        while q:
            rightSide = None                    #to keep track of right child
            
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightSide = node              #update the rightside with node as right side will be the lat inserted
                    q.append(node.left)         #add 1st left and then right
                    q.append(node.right)

            if rightSide:                       #if righSide not null
                res.append(rightSide.val)
        return res
    
    #Time complexity: O(N) since one has to visit each node.

    #Space complexity: O(D) to keep the queues, where D is a tree diameter