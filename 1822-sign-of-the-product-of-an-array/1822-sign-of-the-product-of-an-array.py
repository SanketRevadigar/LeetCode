class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        
        for x in nums:                  # for all elements in nums,if element is  0 return 0, if -ve return -1, else return 1
            if x == 0:
                return 0
            if x < 0:
                 ans *= -1
        
        return ans
    
    # Time- O(N)
    #space- O(1)