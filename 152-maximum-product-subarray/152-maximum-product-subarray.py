class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax,curMin = 1,1
        maxProd = nums[0]
        
        if len(nums) == 0:
            return 0
        
        for n in nums:                      #iterate through numbers
            tmp1 = n * curMin               #calculate current minimum
            tmp2 = n * curMax               #calculate current maximum
            curMax = max(tmp1,tmp2,n)       #max of tmp1 and tmp2 and the present number
            curMin = min(tmp2,tmp1,n)       #min of tmp1 and tmp2 and the present number      
            maxProd = max(maxProd,curMax,curMin)
        return maxProd                      #return the maxProd
        
        
        
        #Time complexity : O(N) where N is the size of nums. The algorithm achieves linear              runtime since we are going through nums only once.

        #Space complexity : O(1) since no additional space is consumed rather than variables             which keep track of the maximum product so far, the minimum product so far, current             variable, temp variable, and placeholder variable for the result.
