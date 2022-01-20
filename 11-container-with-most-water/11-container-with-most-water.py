class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l , r = 0,len(height)-1
        
        while l < r :
            area = (r - l) * min(height[l],height[r])   #calculate area height * distance(breadth)
            res = max(area,res)
            
            if height[l]>height[r]:                     #move the pointer with min height, to increase area of container
                r-=1
            else:
                l+=1
        return res
            
    
    #Time complexity : O(n). Single pass.

    #Space complexity : O(1). Constant space is used.
