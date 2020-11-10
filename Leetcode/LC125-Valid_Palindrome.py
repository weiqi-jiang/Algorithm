class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        if len(s)==1:
            return True
        s = [c.lower()  for c in s if c.isalnum()]
        left = 0
        right = len(s)-1
        while left<=right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
            
        return True