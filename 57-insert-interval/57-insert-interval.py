class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):                             #compare new's end and present interval's start
            if newInterval[1] < intervals[i][0]:                    #if new interval very small, add at 1st
                res.append(newInterval)     
                return res + intervals[i:]                          #return the entire intervals after new
            elif newInterval[0] > intervals[i][1]:                  #compare new's start and present interval's end
                res.append(intervals[i])                            #if small add intervals
            else:
                newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
        res.append(newInterval)                                     #update the newInterval to fit in list
        return res
        
        #Time complexity : O(N) since it's one pass along the input array.

        #Space complexity : O(N) to keep the output.
