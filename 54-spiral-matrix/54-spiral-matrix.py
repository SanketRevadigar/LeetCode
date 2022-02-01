class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROW,COL=len(matrix),len(matrix[0])
        left,top=0,0                                            #initiaise 4 ptrs at 4 corners
        right,bottom=COL,ROW                    
        res=[]
        while left < right and top < bottom:                    #if all ptrs in range
            for i in range(left,right):                         # top row iterating and appending   
                res.append(matrix[top][i])
            top += 1                                            #Increment row as its visited
            
            for i in range(top,bottom):                         #right row iterating
                res.append(matrix[i][right-1])
            right -= 1                                          #right -1 as its visited
            
            if not (left < right and top < bottom):             #check again if all 4ptrs in range
                break
            
            for i in range(right - 1,left - 1, -1):             #bottom row, reverse iterating
                res.append(matrix[bottom - 1][i])
            bottom -= 1                                         #decremnet bottom as its visited
            for i in range(bottom - 1, top - 1, -1):            #finally 1st column
                res.append(matrix[i][left])                     #append and then shift left inwards
            left += 1
        return res