"""
注意进位就行， 最前面补1
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = 1
        for i in range(len(digits)-1,-1,-1):
            value = digits[i]+flag
            if value>=10:
                value -= 10
                flag=1
            else:
                flag = 0
            digits[i] = value
            if not flag:
                break
        if flag:
            digits.insert(0, 1)
        return digits