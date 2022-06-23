class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()                                 #hashmap as a set
        r,l = 0,0                                       #2 pointers fro sliding window
        res= 0
        
        for r in range(len(s)):                         #iterate till end
            while s[r] in charSet:                      #remove all duplicates in set
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])                           #add after removing the duplicates
            res = max(res,r-l+1)                        
        return res
    
    #Time complexity : O(2n)=O(n). In the worst case each character will be visited twice by i and j.

    #Space complexity : O(min(m,n)). Same as the previous approach. We need O(k) space for the sliding window, where kkk      is the size of the Set. The size of the Set is upper bounded by the size of the string n and the size of the              charset/alphabet m.
        