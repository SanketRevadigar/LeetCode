class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS,COLS = len(heights),len(heights[0])                #get rows and cols length & 2 sets for 2 oceans & lst for res
        pac,atl = set(),set()
        res = []                                    
        
        def dfs(r,c,visit,prevHeight):                          #dfs fn to search all squares
            if ((r,c) in visit or                               #if (already in visit or out of bounds or if less than prevHeight)
               r < 0 or c < 0 or r == ROWS or c == COLS or
               heights[r][c] < prevHeight):
                return                                          #exit the function
            visit.add((r,c))                                    #otherwise add to visit, and dfs on all its neighbors
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
        
        for c in range(COLS):                                   #at extereme rows, top to pac,bottom to atl
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])
        
        for r in range(ROWS):                                   #at extereme cols, left to pac, right to atl
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1,atl,heights[r][COLS-1])
        
        for r in range(ROWS):                                   #if any index present in both pac & atl the add to res
            for c in range(COLS):                               #return res
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res