class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l,r = 0,0                                           #2 pointers for sliding window
        count = {}                                          #hashmap to keep track of the max frequency of char
        
        for r in range(len(s)):                             #fill the hashmap
            count[s[r]] = 1+count.get(s[r],0)
        
            while (r - l + 1) - max(count.values()) > k:    #window-maxfrequency of character > k
                count[s[l]] -= 1                            #decrement count 
                l += 1                                      # and shrink window till condition holds good
            res = max(res,r - l + 1)
        return res
        
        #time-O(26*n), we traverse the whole hashmap for maxfrequency
        #space-O(1)