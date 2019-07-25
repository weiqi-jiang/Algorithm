class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        
        maxnumber,minnumber = -float('inf'),float('inf')
        numberCountMap = {}
        for i in range(len(numbers)):
            if numbers[i]== 0:
                continue
            if numbers[i] in numberCountMap:
                return False
            else:
                numberCountMap[numbers[i]] = 1
            maxnumber = max(numbers[i],maxnumber)
            minnumber = min(numbers[i],minnumber)
            
                
        return maxnumber - minnumber < 5