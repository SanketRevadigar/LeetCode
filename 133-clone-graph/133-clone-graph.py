"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        clone = {}                              #hashmap to keep track of copy nodes created
        
        def dfs(node):                          #std dfs function
            if node in clone:
                return clone[node]              #if copy already created return copy
            
            copy = Node(node.val)               #create a new Node with current node value
            clone[node]=copy                    #place inside hashmap
            
            for nei in node.neighbors:          #dfs on all neighbors
                copy.neighbors.append(dfs(nei)) #and append to clone graph
            return copy
        
        return dfs(node) if node else None      #initialise the dfs