class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        lst1=[x for x in range(n+1)]                #create a list of all possible values 
        s_lst1=sum(lst1)                            #take sum of new list and given list    
        s_lst2=sum(nums)
        
        return abs(s_lst1-s_lst2)                   #return the missing value by taking the difference
    
    
    #Time Complexity: O(2N) 2 times sum
    #Space Complexity:O(1)
        
    
                    
            