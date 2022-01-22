class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        for i in range(len(s)):                             #iterate through s
            l = r = i                                       #for odd length set l=r=i
            while (l >= 0 and r < len(s) and s[l] == s[r]): #check the bounds and if they are equal or not
                res += 1                                    #increment res if conditions holds true
                l -= 1                                      #decrement left and increment right
                r += 1
            
            l,r = i,i+1                                     #similarlly for even length l=i & r=i+1 
            
            while (l >=0 and r < len(s) and s[l] == s[r]):
                res += 1
                l -= 1
                r += 1
        
        return res
    
    #Time Complexity:O(N^2) for input string of length N
    #Space Complexity: O(1). We don't need to allocate any extra space since we are repeatedly iterating on the input           string itself.
                
                
        
        