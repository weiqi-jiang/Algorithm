class Solution:
    def InversePairs(self, data):
        # write code here
        count = [0]
        self.helper(data,count)
        return count[0]%1000000007
        
        
    def helper(self,nums,count):
        if len(nums)<=1:
            return nums
        mid = len(nums)//2
        return self._merge(self.helper(nums[:mid],count),self.helper(nums[mid:],count),count)
        
        
        
    def _merge(self,n1,n2,count):
        p1,p2 = 0,0
        res = []
        while p1<len(n1) and p2<len(n2):
            if n1[p1]<=n2[p2]:
                res.append(n1[p1])
                p1+=1
            else:
                count[0]+= len(n1[p1:])
                res.append(n2[p2])
                p2+=1
        res += n1[p1:]
        res += n2[p2:]
        return res