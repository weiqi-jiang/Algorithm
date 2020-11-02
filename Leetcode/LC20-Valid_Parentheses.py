"""
stack 维护一个栈，如果opening bracket 压入栈
否则判断当前元素是否和栈顶opening bracket of the same type
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cur_top = []
        for p in s:
            if p in ("(", '{', '['):
                cur_top.append(p)
                stack.append(-1)
            else:
                if not cur_top:
                    return False
                if p == ')' and cur_top[-1] == '(':
                    stack.append(1)
                    cur_top.pop()
                elif p == '}' and cur_top[-1] == '{':
                    stack.append(1)
                    cur_top.pop()
                elif p == ']' and cur_top[-1] == '[':
                    stack.append(1)
                    cur_top.pop()
                else:
                    return False 
        return sum(stack) == 0
                