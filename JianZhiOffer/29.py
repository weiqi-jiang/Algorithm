class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        curmode,count = numbers[0],0
        for i in range(len(numbers)):
            if numbers[i] == curmode:
                count+=1
            else:
                count -=1
                if not count:
                    curmode  = numbers[i]
                    count = 1
        count = 0
        for i in range(len(numbers)):
            if numbers[i] == curmode:
                count+=1
        if count>len(numbers)/2:
            return curmode
        else:
            return 0