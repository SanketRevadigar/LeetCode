class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,len(numbers)-1
        
        while l <= r:
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            elif numbers[l] + numbers[r] > target:          #if sum > target decrement from right
                r -= 1
            else:                                           ##if sum > target increment from left
                l += 1
                
         #time-O(n)
        #space-O(1)
        