class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap={}                                         #hashmap to store nums and its index
        for i,n in enumerate(nums):                     #enumerate fn to iterate both i & n, i=index,n=number 
            diff=target-n                               
            if diff in hmap:
                return (hmap[diff],i)                   #return value of hmap and index
            hmap[n]=i                                   #mark in hmap
            
        