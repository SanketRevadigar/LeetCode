class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        
        for i , a in enumerate(nums):               #'a' will be our first number
            if i > 0 and a == nums[i-1]:
                continue
            
            l,r = i+1,len(nums)-1
            
            while l < r:                            #running twosum II for other 2 values
                threeSum = a + nums[l] + nums[r]
                
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums [l-1] and l < r:  #updating only 1 pointer as the above conditions take care of other
                        l += 1
        return res
    
    
    
    #time-O(n^2)twoSumII is O(n),and we call it nnn times.Sorting the array takes O(nlog⁡n)so overall complexity is             O(nlogn+n2). This is asymptotically equivalent to O(n2)\mathcal{O}(n^2)O(n2)
    #space-O(1) or O(n)
                