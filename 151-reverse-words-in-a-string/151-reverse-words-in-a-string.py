class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
    
    #first split the string, then reverse the list of splitted words, and later join back the list to string
    #split handles the beginning and ending extra spaces
    
    #Time-O(N)
    #Space-O(N)