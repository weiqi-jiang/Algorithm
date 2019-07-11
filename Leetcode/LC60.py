class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        res = []
        self.helper(res,[i for i in range(1,n+1)],k)
        
        return ''.join(res)
        
        
        
        
    def helper(self,res,nums,k):
        if  len(nums)<=1:
            res.append(str(nums[0]))
            return 
        c = self.factorial(len(nums)-1)
        cur_count = 0
        for i in range(len(nums)):
            cur_count += c
            if cur_count>=k:
                res.append(str(nums.pop(i)))
                
                self.helper(res,nums,k-(cur_count-c))
                break
    
    def factorial(self,n):
        c = 1
        for i in range(1,n+1):
            c*=i
        return c