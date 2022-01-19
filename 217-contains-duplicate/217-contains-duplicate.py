class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hmap = {}
        
        for i,n in enumerate(nums):         #i=index,n=nums
            if n in hmap:
                return True
            hmap[n] = i
        return False
        
        

    #Time complexity: O(n). We do search() and insert() for nnn times and each operation takes constant time.

    #Space complexity: O(n). The space used by a hash table is linear with the number of elements in it.
