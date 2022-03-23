class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:                     #Calculating distance from origin for all points
            dist = (x**2) + (y**2)
            minHeap.append([dist,x,y])          #append to list, the dist and x,y pints
        
        heapq.heapify(minHeap)                  #convert list to heap using heapify()
        res= []
        while k > 0:                            #pop the heap from top as it stores the lowest value
            dist,x,y=heapq.heappop(minHeap)     #append only distance to res, and decrement k
            res.append([x,y])
            k -= 1
        return res                              #return res
    
    #Time -O(N)
    #Space -O(N)