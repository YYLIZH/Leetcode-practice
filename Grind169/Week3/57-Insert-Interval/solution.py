from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res = []
        for index, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif newInterval[1] < interval[0]:
                res.append(newInterval)
                newInterval = interval
            else:  # overlap case
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        res.append(newInterval)
        return res
