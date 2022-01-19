class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1                             #pre to product res from front
        post = 1                            #post to product res from back
        res = [1] * len(nums)
        
        for i in range(len(nums)):          #multiplying to res from front       
            res[i] = pre                
            pre = pre * nums[i]
        
        for i in range(len(nums)-1,-1,-1):  #multipying to updated res from pre with post from behind
            res[i]*=post
            post=post*nums[i]
    
        return res
                       
       #Time complexity : O(N) where N represents the number of elements in the input array. We use one iteration         to construct the array L, one to construct the array R and one last to construct the answer array using L         and R.
       #Space complexity : O(N) used up by the two intermediate arrays that we constructed to keep track of               product of elements to the left and right.  
        