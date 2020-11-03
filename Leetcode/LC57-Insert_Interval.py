"""
LC56的变种，只需要把newInterval append进intervals 排序，然后就和LC56一模一样了
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals:
            return [newInterval]
        all_intervals = intervals + [newInterval]
        all_intervals = sorted(all_intervals, key=lambda _: _[0])
        res  =[]
        for i in range(len(all_intervals)):
            if not res:
                res.append(all_intervals[i])
            else:
                if all_intervals[i][0]<=res[-1][1]:
                    res[-1][1] = max(res[-1][1],all_intervals[i][1])
                else:
                    res.append(all_intervals[i])
        return res