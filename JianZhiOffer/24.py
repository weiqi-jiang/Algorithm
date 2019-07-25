class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        return self.postorder(sequence)
        
        
    def postorder(self,sequence):
        if len(sequence)<=1:
            return True
        root = sequence[-1]
        index = 0
        while sequence[index]<root:
            index += 1
        for i in range(index,len(sequence)-1):
            if sequence[i]<root:
                return False
        left = self.postorder(sequence[:index])
        right = self.postorder(sequence[index:-1])
        return right and left