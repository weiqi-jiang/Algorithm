"""
recursive approach
1. 从index=0开始 找到回文字符，剩下的字符迭代下一轮
2. 如果最后一轮迭代剩余字符为空，说明可能原始字符可以完整的分成若干个回文，append 进最后结果array
"""
class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return [[]]
        res = []
        self.help(s,[],res)
        return res
        
    def help(self,s,cur,res):
        for i in range(len(s)):
            if self.isPalindrome(s[:i+1]):
                if i==len(s)-1:
                    res.append(cur+[s])
                    return 
                self.help(s[i+1:],cur+[s[:i+1]],res)
    
    def isPalindrome(self,s):
        if not s:
            return True
        left,right = 0,len(s)-1
        while left<=right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True