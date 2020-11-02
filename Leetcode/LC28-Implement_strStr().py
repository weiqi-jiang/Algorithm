"""
注意haystack[i+j]这里不要超出index
优化点在于不需要判断最后len(needle)，因为已经不可能出现完全匹配的，长度不够。
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if len(needle)> len(haystack):
            return -1
        
        for i in range(len(haystack)-len(needle)+1):
            flag = True
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    flag = False
                    break
            if flag:
                return i
        return -1