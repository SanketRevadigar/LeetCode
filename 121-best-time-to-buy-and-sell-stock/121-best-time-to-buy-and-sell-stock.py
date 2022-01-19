class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right = 0,1
        maxProfit = 0
        
        while right < len(prices):                          
            
            if prices[right] > prices[left]:                        #comapre the prices
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit,profit)
            else:
                left = right                                        #shift the left pointer to right location
            right+=1       
            
        return maxProfit
                
            
      
    #Time complexity: O(n). Only a single pass is needed.

    #Space complexity: O(1). Only two variables are used.
  
        
        