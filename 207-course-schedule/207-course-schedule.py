class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:                   #create hashmap with course,prereq, and fill it
            preMap[crs].append(pre)
            
        visit = set()
        def dfs(crs):                                   #dfs function on crs
            if crs in visit:                            #if crs in visit, then false
                return False
            if preMap[crs] == []:                       #if crs doesnt have any pre return true
                return True
            
            visit.add(crs)                              #if both condition fails, add crs to visit
            for pre in preMap[crs]:                     #for prereq, check again they have any prereq
                if not dfs(pre):                        #if yes, return False
                    return False
            visit.remove(crs)                           #as the crs is processed remove from visit
            preMap[crs] = []
            return True
        for crs in range(numCourses):                   #for all crs provided run dfs
            if not dfs(crs):
                return False
        return True
    
    
    #Time :-O(N+P), N-Courses,P-Prerequisites
    #Space :-O(N+P), N-Courses,P-Prerequisites