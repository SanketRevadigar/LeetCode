class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        q = collections.deque()                                 #len of row,col and q to append values and set to track visited
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        def bfs(r,c):
            q.append((r,c))                                     #iterative BFS using queue
            visit.add((r,c))
            while q:
                R,C = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]        #first check if the other neighbours are in range
                for dr,dc in directions:                        #check if its value is 1, and is not in visit
                    row,col = R+dr,C+dc
                    if (row in range(ROWS) and col in range(COLS) and grid[row][col] == "1" and (row,col) not in visit):
                        q.append((row,col))                     #add to visit set & queue
                        visit.add((row,col))
               
        for r in range(ROWS):
            for c in range(COLS):                               #run bfs on all nodes, and add to res 
                if (grid[r][c] == "1" and (r,c) not in visit):
                    bfs(r,c)
                    res += 1
        return res
    
    
    #Space and Time -O(N)