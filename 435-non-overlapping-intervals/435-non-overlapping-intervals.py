class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        prevEnd = intervals[0][1]                                   #end of last element
        
        for start,end in intervals[1:]: 
            if start >= prevEnd:                                    #if they are not overlapping update prevEnd ptr to new end
                prevEnd = end
            else:
                res += 1                                            #if overlapping add 1 to res and change the prevEnd to
                prevEnd = min(prevEnd,end)                          #determine which element to remove, we remove the interval
                                                                    #with min end so that it doesnt conflict again
        return res
        
        
        #Time complexity : O(nlog⁡(n)). Sorting takes O(nlog⁡(n) time.

        #Space complexity : O(1). No extra space is used.
