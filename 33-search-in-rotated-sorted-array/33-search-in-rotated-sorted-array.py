class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] >= nums[start]:                      #search in left side
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
                    
            else:                                                ##search in right side
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1
        
        
        #Time complexity: O(log⁡N)\mathcal{O}(\log{N})O(logN).
        #Space complexity: O(1)\mathcal{O}(1)O(1).
