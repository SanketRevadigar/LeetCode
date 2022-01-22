class Solution:
    def isPalindrome(self, s: str) -> bool:
        New=""                              #new variable to store the updated string
        for char in s:                      #check every character if its alphanumeric
            if char.isalnum():              #if its alnum add to new string
                New += char.lower()
        return New == New[::-1]             #check the new string with its reversed form
    
    #Time complexity : O(n), in length nnn of the string.
    #Space complexity :O(n), in length nnn of the string.
        