"""
滑动窗口的思路：
维护一个滑动窗口，窗口内不包含重复字符
优化点在于如何快速的找到窗口中是否有重复元素，而且重复的元素index是多少
"""
# 使用find
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

# 不使用find
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        window = []
        length = 0
        for c in s:
            flag = False
            for i in range(len(window)):
                if window[i] == c:
                    window = window[i+1:] + [c]
                    length = max(length, len(window))
                    flag = True
                    break
            if not flag:
                window = window + [c]
                length = max(length, len(window))
        return length