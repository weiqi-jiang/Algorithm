class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        stat = [False for i in range(N+1)]
        for i in range(2,N+1):
            for j in range(1,i//2+1):
                if i%j == 0 and stat[i-j] == False:
                    stat[i] = True
        return stat[N]