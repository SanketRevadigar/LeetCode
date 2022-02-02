class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()                                        #sort the intervals
        output = [intervals[0]]                                 #append first interval 
        
        for start,end in intervals[1:]:                         #iterate throughout intervals
            lastEnd = output[-1][1]                               #access the last interval's end
            
            if start <= lastEnd:                                  #if start of present interval less than lastEnd
                output[-1][1] = max(lastEnd,end)                  #change the end in output
            else:
                output.append([start,end])                        #append the next interval
        return output
        
        #Time complexity : O(nlog⁡n) #sort=O(logN),Linear scan- O(N)   
        #Space complexity : O(log⁡N) #sorting takes O(logN)