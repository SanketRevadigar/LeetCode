class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2                #modding tells whether the last bit is 1 or 0, if 1 res will be updated
            n = n >> 1                  #shift the bits by 1 to check the next bit
        return res
    
    
    #Time complexity-O(1)
    #Space complexity-O(1)