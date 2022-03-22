class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        cntA, cntB, cntC = 0, 0, 0 # used to count the occurrences of corresponding character 
        for i in range(a+b+c):      
            maxCount = max(a, b, c)         #get max every iteration
            if (a == maxCount and cntA < 2) or (cntB == 2 and a >= 1) or (cntC == 2 and a >= 1):
                res.append('a')
                a = a-1
                cntA = cntA+1
                cntB, cntC = 0, 0
            elif (b == maxCount and cntB < 2) or (cntA == 2 and b >= 1) or (cntC == 2 and b >= 1):
                res.append('b')
                b = b-1
                cntB = cntB+1
                cntA, cntC = 0, 0
            elif (c == maxCount and cntC < 2) or (cntA == 2 and c >= 1) or (cntB == 2 and c >= 1):
                res.append('c')
                c = c-1
                cntC = cntC+1
                cntA, cntB = 0, 0
        # end loop

        return "".join(res)
        