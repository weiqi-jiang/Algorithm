class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array or not array[0]:
            return False
        i,j = len(array)-1,0
        
        while True:
            if array[i][j] == target:
                return True
            if array[i][j]<target:
                if j<len(array)-1:
                    j+=1
                    continue
                else:
                    return False
            if array[i][j]>target:
                if i>0:
                    i-=1
                    continue
                else:
                    return False