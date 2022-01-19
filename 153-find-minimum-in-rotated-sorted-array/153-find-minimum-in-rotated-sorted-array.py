class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # If the list has just one element then return that element.
        if len(nums)==1:
            return nums[0]
        
        left,right=0,len(nums)-1
        
        # if the last element is greater than the first element then there is no rotation.
        # so first element will be smallest
        if nums[right] > nums[0]:
            return nums[0]
        
        while left <= right:                    #binary search  
            mid=(left + right)//2
            
            # if the mid element is greater than its next element then mid+1 element is the smallest
            # This point would be the point of change. From higher to lower value.
            if nums[mid] > nums[mid+1]:     
                return nums[mid+1]
            
            # if the mid element is lesser than its previous element then mid element is the smallest
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            
            # if the mid elements value is greater than the 0th element this means the least value is still
            #  somewhere to the right as we are still dealing with elements greater than nums[0]
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1
        
        
        
        #Time Complexity : Same as Binary Search O(log⁡N)O(\log N)O(logN)
        #Space Complexity : O(1)O(1)O(1)