
"""
horizontal scanning 
longest common prefix（LCP） = LCP(LCP(LCP(S1,S1),S3),S4)

"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
       
        def helper(s1, s2):
            if not s1 or not s2:
                return ""
            res = ""
            i, j = 0,0 
            while i <len(s1) and j<len(s2):
                if s1[i] == s2[j]:
                    res+=s1[i]
                    i+=1
                    j+=1
                else:
                    break
            return res

        cur = helper(strs[0], strs[1])
        strs = strs[2:]
        while strs:
            next_str = strs.pop(0)
            cur = helper(cur, next_str)
        return cur 
        
"""
思路二：vertical scanning 竖着扫描，好处就是最短的那个字段决定着最大的搜索次数，
先看所有字符串的index=0元素是否相同，
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        lengths = [len(s) for s in strs ]
        if not lengths:
            return ""
        max_common_length = min(lengths)
        if max_common_length ==0:
            return ""
        index = 0
        res = ""
        while index <max_common_length:
            temp = [s[index] for s in strs]
            if len(set(temp)) ==1:
                res += strs[0][index]
                index += 1
            else:
                break
        return res
"""
思路三： 这是一个divide and conquer 的问题，LCP(LCP(left),LCP(right))
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        
        def helper(s1, s2):
            if not s1 or not s2:
                return ""
            res = ""
            i, j = 0,0 
            while i<len(s1) and j<len(s2):
                if s1[i] == s2[j]:
                    res+=s1[i]
                    i+=1
                    j+=1
                else:
                    break
            return res
 
        def LCP(strs):
            if len(strs)==1:
                return strs[0]
            if len(strs)== 2:
                return helper(strs[0],strs[1])

            mid = len(strs)//2
            left = strs[:mid]
            right = strs[mid:]
            return helper(LCP(left), LCP(right))
        
        return LCP(strs)
            