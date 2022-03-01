class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)                              #create a set of nums
        for n in nums:                                  #iterate through list and check if n is the starting no in sequence
            if (n-1) not in numSet:                     #if its left(n-1) value is not their in set it means its the start
                length = 0                              #initialise length and check its next numbers(n+0,n+1,n+2...)
                while (n+length) in numSet:             #if its next nos not in list then return the current length
                    length += 1
                longest = max(longest,length)           #if next nos are in set, keep increasing length and return the max
        return longest
        
        
        #Time-O(N) Set
        #Space-O(N) Single pass