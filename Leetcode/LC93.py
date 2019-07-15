class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        temp,res = [],[]
        self.helper([],temp,s)
        for t in temp:
            ifzero = [n.startswith('0') and len(n)>1 for n in t]
            if True not in ifzero:
                res.append('.'.join(t))
                    
        return res
        
    def helper(self,cur,res,s):

        if len(cur) == 4:
            if not s:
                res.append(cur)
            else:
                return 
        for i in range(1,min(4,len(s)+1)):
            if int(s[:i]) <=255:
                self.helper(cur+[s[:i]],res,s[i:])