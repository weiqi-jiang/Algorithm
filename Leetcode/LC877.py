class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        matrix = [[0 for i in range(len(piles))] for j in range(len(piles))]
        for i in range(len(piles)):
            matrix[i][i] = piles[i]
        s = [n for n in piles]
        for i in range(1,len(piles)):
            s[i] += s[i-1]
        for i in range(1,len(piles)):
            n = i
            m = 0
            while n <len(piles):
                rightsum = piles[n] + s[n-1] - matrix[m][n-1]
                leftsum = piles[m] + s[-1]-s[m] - matrix[m+1][n]
                matrix[m][n]  = max(rightsum,leftsum)
                n += 1
                m += 1
        
        return matrix[0][len(piles)-1]>sum(piles)/2