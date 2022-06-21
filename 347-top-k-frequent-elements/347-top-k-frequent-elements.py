class Solution:
    def topKFrequent(self, nums, k) :
        map=Counter(nums) # counter is used to count the frequency of each element
        result=[]
        for key,value in map.items():
            result.append([key,value])
        result.sort(key=lambda x:x[1],reverse=True) # sort with respect to the second element in the list
        return [x[0] for x in result[:k]] # return the first k elements in the list