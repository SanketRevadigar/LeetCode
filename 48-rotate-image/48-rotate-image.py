class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left,right=0,len(matrix)-1                              #4 ptrs at 4 ends
        top,bottom = left,right
        
        while left < right:                                     #while in boundries
            for i in range(right - left):                       #top swap all nos
                topLeft = matrix[top][left + i]                 #variable to store 1st element
                matrix[top][left + i] = matrix[bottom - i][left]    #swapping from reverse
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = topLeft                
            left += 1                                           #adjusting the pointers
            right -= 1
            top += 1
            bottom -= 1