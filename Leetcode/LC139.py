class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        isvalid = [False for i in range(len(s))]
        for i in range(len(s)):
            for w in wordDict:
                if i>= len(w)-1 and s[i+1-len(w):i+1] == w and (isvalid[i-len(w)] or i+1-len(w)==0):
                    isvalid[i] = True
        return isvalid[-1]