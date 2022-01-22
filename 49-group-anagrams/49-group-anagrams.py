class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}                                      #*
        for words in strs:
            sortedWord = ' '.join(sorted(words))
            if sortedWord not in count:
                count[sortedWord] = [words]
            else:
                count[sortedWord].append(words)
        return count.values()
    '''
        final = []
        for word in count.values():
            final.append(word)
        return final
        '''