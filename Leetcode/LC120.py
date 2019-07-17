class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return 
        for level in range(1,len(triangle)):
            for i in range(len(triangle[level])):
                if i == 0:
                    triangle[level][0] += triangle[level-1][0]
                elif i == len(triangle[level])-1:
                    triangle[level][i] += triangle[level-1][-1]
                else:
                    triangle[level][i] += min(triangle[level-1][i],triangle[level-1][i-1])
        print(triangle)
        return min(triangle[-1])