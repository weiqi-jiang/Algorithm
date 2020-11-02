"""
“嵌套全排列问题”
opening 剩下没用的开括号
closing 剩下没用的比括号
balance 开括号+1 闭括号-1 只有在balance >0的时候才能使用闭括号
cur 记录当前字符
res 保留最后结果
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        res = []
        def helper(opening, closing, balance, cur,res):
            if not opening and not closing:
                res.append(cur)
                return
            if opening:
                helper(opening-1,closing, balance+1, cur+'(',  res)
            if closing and balance>0:
                helper(opening, closing-1, balance-1, cur+')', res)
        
        helper(n,n,0,'',res)
        return res