class Solution:
    def countBits(self, num: int) -> List[int]:
        left = 2
        right = 2*2
        if num == 0:
            return [0]
        if num == 1:
            return [0,1]
        stat = [0 for i in range(num+1)]
        stat[0],stat[1] = 0, 1
        cur = 2
        flag = True
        while flag:
            while cur < right:
                stat[cur] = stat[cur-left]+ 1
                cur+=1
                if cur>num:
                    flag = False
                    break
                    
            left = right
            right = right*2
        return stat
		
# 更加优雅的解法
def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        iniArr = [0]
        if num > 0:
            amountToAdd = 1
            while len(iniArr) < num + 1:
                iniArr.extend([x+1 for x in iniArr])
        
        return iniArr[0:num+1]