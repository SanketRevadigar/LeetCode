class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols=len(board),len(board[0])
        path=set()
        
        def dfs(r,c,i):                                             #helper function
            if i == len(word):                                      #if i equals word len, means word found
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c] or (r,c) in path:
                return False                                        #check all the conditions
            
            path.add((r,c))                                         #add path, for not to visit again
            res = (dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1))
            path.remove((r,c))                                      #call dfs on neighbours and remove path 
            return res
        for r in range(rows):                                       #call dfs on all elements
            for c in range(cols):
                if dfs(r,c,0): return True
        return False
            
        
    #Time Complexity: O(N⋅3L) where N is the number of cells in the board and L is the length of the word to be matched.
    #For the backtracking function, initially we could have at most 4 directions to explore, but further the choices are        reduced into 3 (since we won't go back to where we come from). As a result, the execution trace after the first step      could be visualized as a 3-ary tree, each of the branches represent a potential exploration in the corresponding          direction. Therefore, in the worst case, the total number of invocation would be the number of nodes in a full 3-nary      tree, which is about 3L.We iterate through the board for backtracking, i.e. there could be NNN times invocation for        the backtracking function in the worst case.
    #Space Complexity: O(L) where LLL is the length of the word to be matched

        