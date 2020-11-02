"""
解法： HashMap
难点在于怎么找到一个固定不变的key
solution1：categorize by sorted string, sorted(word) 作为key， 相同字母不同字符顺序拥有相同的key
solution2：categorize by count key是26个0，如果一个字母出现一次就在对应位置上置1
"""
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