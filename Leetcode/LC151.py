class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        s = [n for n in s]
        i = 0
        while i < len(s):
            if s[i]==' ' and s[i-1] == ' ':
                s.pop(i)
            else:    
                i += 1
        temp = ''.join(s)
        return ' '.join(temp.split(' ')[::-1])