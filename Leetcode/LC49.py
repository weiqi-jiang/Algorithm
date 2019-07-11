class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for word in strs:
            words = ''.join(sorted(word))
            if words in dict.keys():
                dict[words].append(word)
            else:
                dict[words] = []
                dict[words].append(word)
        output = []
        for words,value in dict.items():
            output.append(value)
        return output