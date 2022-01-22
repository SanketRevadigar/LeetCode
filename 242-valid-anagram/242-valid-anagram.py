class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):                        #if both strings are not equal return false
            return False
        hashmap = {}                                
        for i in s:                                 #fill hashmap for 1st string
            hashmap[i] = 1 + hashmap.get(i,0)
        
        for r in t:                                 #decrement the same hashmap
            if r in hashmap:
                hashmap[r] -= 1
        res = max(hashmap.values())                 #if no values in hashmap,means all letters in s exists in t
        return True if res == 0 else False          #return true if res=0
        
        
        #time- O(N) because accessing the counter table is a constant time operation.
        #space-O(1) Although we do use extra space, the space complexity is O(1) because the table's size stays constant            no matter how large nnn is.