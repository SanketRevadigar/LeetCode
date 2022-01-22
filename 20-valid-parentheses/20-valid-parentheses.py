class Solution:
    def isValid(self, s: str) -> bool:
        valid = {')':'(','}':'{',']':'['}           #key value pairs
        stack = []                      
        for char in s:                              #iterate through each char
            if char in valid:                       #if its a closing bracket
                top=stack.pop() if stack else None  #pop its matching opening bracket if present
                if valid[char] != top:              #if matching opening bracket not found
                    return False                    #return false
            else:
                stack.append(char)                  #if its a opening bracket append to stack
        return not stack                            #if stack empty true else false
            
            
        #Time complexity :O(n) because we simply traverse the given string one character at a time and              push and pop operations on a stack take O(1) time.
        #Space complexity :O(n) as we push all opening brackets onto the stack and in the worst case, we            will end up pushing all the brackets onto the stack. e.g. ((((((((((
        