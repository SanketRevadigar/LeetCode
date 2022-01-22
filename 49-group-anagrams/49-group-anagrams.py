class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}                                      #hashmap for key values
        for words in strs:                              #sort each word and add as a key
            #sortedWord = ' '.join(sorted(words))        #use join to add word as str,dont assign directly
            if str(sorted(words)) not in count:
                count[str(sorted(words))] = [words]
            else:
                count[str(sorted(words))].append(words)
        return count.values()