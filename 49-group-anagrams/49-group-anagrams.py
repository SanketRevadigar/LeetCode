class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}                                      #hashmap for key values
        for words in strs:                              #sort each word and add as a key
            sortedWord = ' '.join(sorted(words))        #use join to add word as str,dont assign directly
                                                        # or use type casting as str(sorted(words))
            if sortedWord not in count:                 #if SortedWord not in count add it as key &      
                count[sortedWord] = [words]             #add original word as its value
            else:
                count[sortedWord].append(words)         #if already present add it as its value
        return count.values()                           #return values