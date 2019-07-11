class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = []
        for c in s:
            if c=='(' or c=='[' or c=='{':
                temp.append(c)
            else:
                if not temp:
                    return False
                if c==')':
                    if temp[-1]=='(':
                        temp.pop()
                    else:
                        return False
                if c=='}':
                    if temp[-1]=='{':
                        temp.pop()
                    else:
                        return False
                if c==']':
                    if temp[-1]=='[':
                        temp.pop()
                    else:
                        return False
        if not temp:
            return True
        else:
            return False