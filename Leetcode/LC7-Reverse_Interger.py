"""
steps:
1: 保留符号
2：数值型转字符串
3：reverse 字符串
4：判断是否越界
"""
class Solution:
    def reverse(self, x: int) -> int:
        sign  = 1 if x>0 else -1
        x = x if x>0 else x*-1
        s = str(x)
        s = s[::-1]
        res = sign * int(s)
        if res< -2**31 or res>2**31-1:
            return 0
        return res