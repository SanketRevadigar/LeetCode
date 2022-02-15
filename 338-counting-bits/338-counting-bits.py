class Solution:
    def countBits(self, n: int) -> List[int]:
        counter = [0]
        for i in range(1,n+1):                        # looping through all numbers
            counter.append(counter[i>>1]+i%2)     #https://leetcode.com/problems/counting-bits/discuss/656849/Python-Simple-Solution-with-Clear-Explanation
        return counter
            
        
        
        #Time: O(n) - We iterate through the range of numbers once.
        #Space: O(n) - We use a num-sized array.