class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""                                    #res for subsstring and reslen for length
        reslen = 0
        
        for i in range(len(s)):                     #iterate all s
            l,r = i,i                               #for odd case l,r=i,i
            while(l >= 0 and r < len(s) and s[l] == s[r]):      #check the if in bounds and are equal
                if(r - l +1)>reslen:                #if the new window is greater than previous
                    reslen = r - l +1               #update reslen and res
                    res = s[l:r+1]
                l -= 1                              #move out from center,decrement left and 
                r += 1                              #increment right
                
            l,r = i,i+1                             #similarlly for even length but r=i+1
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                if(r - l + 1) > reslen:
                    reslen = r- l +1
                    res = s[l:r+1]
                l -= 1
                r += 1
        return res
            
        
        #Time complexity : O(n2). Since expanding a palindrome around its center could take O(n) time,              the overall complexity is O(n2).

        #Space complexity :O(1). 