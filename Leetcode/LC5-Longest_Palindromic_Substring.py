"""
思路： 
对每个元素，从该元素向两边展开，直到不是回文字符，记录最大值。当然这有两种情况
以一个元素为中心的回文，和以两个元素为中心的回文。所以要重复两次判断。
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res= ""
        for i in range(len(s)):
            temp = self.findPalindromic(i,i,s)
            if len(temp)>len(res):
                res = temp
        for i in range(len(s)-1):
            temp = self.findPalindromic(i,i+1,s)
            if len(temp)>len(res):
                res = temp
        return res
        
    def findPalindromic(self,left,right,s):
        while s[left] == s[right]: 
            if left>0 and right<len(s)-1:
                left -= 1
                right += 1
            else:
                return s[left:right+1]
        return s[left+1:right]