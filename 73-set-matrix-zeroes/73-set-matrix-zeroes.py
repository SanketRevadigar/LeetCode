class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        Rows,Cols = len(matrix), len(matrix[0])             #Get ROW & COL length
        rowZero = False                                     #take variable to check position[0][0]
        
        for r in range(Rows):                               #Iterate through matrix
            for c in range(Cols):
                if matrix[r][c] == 0:                       #if any value in matrix is 0, set its 1st row and its col as 0
                    matrix[0][c] = 0                        #but we do that only if  row is not 1st row
                    if r > 0:                               #if row not 1st row set 1st col also as 0
                        matrix[r][0] = 0
                    else:                                   #for topleft position set variables as true
                        rowZero = True
        
        for r in range(1,Rows):                             #now set all row and col as zero
            for c in range(1,Cols):
                if matrix[0][c] == 0 or matrix [r][0] == 0: #checking if its row/col is 0 set entire row/col as 0
                    matrix[r][c] = 0
                
        if matrix [0][0] == 0:                              #but for topleft position,we need to check separately
            for r in range(Rows):                           #first set all 1st column values as 0
                matrix[r][0] = 0
        
        if rowZero:                                         #if variable is true set its all row as 0
            for c in range(Cols):
                matrix[0][c] = 0