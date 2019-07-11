class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = ""
        MaxLength = 0
        for i in range(len(s)):
            index = res.find(s[i])
            if index == -1:
                res += s[i]
            else:
                if index == len(s)-1:
                    res = res[i]
                else:
                    res = res[index+1:]+s[i]
            MaxLength = max(MaxLength, len(res))
        return MaxLength