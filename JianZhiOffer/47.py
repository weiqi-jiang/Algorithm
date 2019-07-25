class Solution:
    def Add(self, num1, num2):
        # write code here
        
        while num2!=0:
            s = (num1 ^ num2) & 0xFFFFFFFF
            carry = ((num1&num2)<<1)& 0xFFFFFFFF
            num1 = s
            num2 = carry
        return num1 if num1<=0x7FFFFFFF else ~(num1^0xFFFFFFFF)