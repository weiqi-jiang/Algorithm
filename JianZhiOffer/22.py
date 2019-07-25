class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here

        
        return self.helper(pushV,popV)
        
    def helper(self,pushorder,poporder):
        helpstack = []
        i=0
        while True:
            
            target = poporder[i]
            if not pushorder and helpstack and helpstack[-1]!=target:
                return False
            if helpstack and helpstack[-1] == target:
                i+=1
                helpstack.pop()
            else:
                if pushorder:
                    cur = pushorder.pop(0)
                    helpstack.append(cur)
            if i>=len(poporder):
                return True