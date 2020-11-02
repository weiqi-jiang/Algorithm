"""
在穷尽所有可能性下的递归方式，考察的是耐心
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        
        def helper(nums, res):
            if nums == 0:
                return res
            
            if nums<4:
                res += nums * "I"
                return res
            
            if nums == 4:
                res += "IV"
                return res
            
            if nums <9 and nums>=5:
                return helper(nums-5, res+'V')
                
            if nums == 9:
                res += 'IX'
                return res    

            if nums >=10 and nums<40:
                return helper(nums-10, res +'X')

            if nums >= 40 and nums <50:
                return helper(nums-40, res +'XL')

            if nums >= 50 and nums < 90:
                return helper(nums-50, res + 'L')

            if nums >=90 and nums<100:
                return helper(nums-90, res+'XC')
            
            if nums>=100 and nums<400:
                return helper(nums-100, res + 'C')
                
            if nums >=400 and nums<500:
                return helper(nums-400, res + 'CD')
                
            if nums>=500 and nums<900:
                return helper(nums-500, res + 'D')
            
            if nums>=900 and nums<1000:
                return helper(nums-900, res +'CM')
            
            if nums >= 1000:
                return helper(nums-1000, res +'M')
        
        return helper(num, '')