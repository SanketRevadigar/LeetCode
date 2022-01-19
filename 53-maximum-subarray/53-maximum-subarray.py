class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0                              #to store the current sum
        maxSum = nums[0]                        # to store max sum
        
        if len(nums) == 0:
            return 0
        
        for n in nums:                          #iterate through numbers
            if curSum < 0:
                curSum = 0                      #set curSum to 0, if sum is less than 0
            curSum += n                         #add num to curSum
            maxSum = max(curSum,maxSum)
        return maxSum                           #return the max of both
        
        
        #Time complexity: O(N), where N is the length of nums.We iterate through every element          of nums exactly once.

        #Space complexity: O(1) No matter how long the input is, we are only ever using 2               variables: curSum and maxSum.
