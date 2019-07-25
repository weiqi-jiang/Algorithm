class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        res = set()
        for index in range(len(ss)):
            self.generatePermutation(ss[index],[],res,ss[:index]+ss[index+1:])
        return sorted(list(res))
        
    def generatePermutation(self,cur,permutation,res,ss):
        permutation = permutation +[cur]
        if not ss:
            res.add(''.join(permutation))
            return 
        for index in range(len(ss)):
            self.generatePermutation(ss[index],permutation,res,ss[:index]+ss[index+1:])