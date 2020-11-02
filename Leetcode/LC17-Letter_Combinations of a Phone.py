"""
思路：
经典的递归全排列
keys:
1. 维护当前结果， 维护一个全局list 存放最终结果
2. 判断是否递归结束，如果结束当前结果存入list
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {
            '2':["a","b","c"],
            '3':["d","e","f"],
            '4':["g","h","i"],
            '5':["j","k","l"],
            '6':["m",'n','o'],
            '7':["p",'q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
            
        }
        res = []
        if len(digits)<1:
            return []
        self.find(digits,0,"",res,m)
        return res
        
    def find(self,digits,index,temp,res,m):
        
        for c in m[digits[index]]:
            if index == len(digits)-1:
                res.append(temp + c)
            else:
                self.find(digits,index+1,temp+c,res,m)