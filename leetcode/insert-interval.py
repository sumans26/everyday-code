# https://leetcode.com/problems/insert-interval/



def insert(self, intervals, newInterval):
    """
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """
    left = []
    right = []

    for interval in intervals:
        if(interval[1] >= newInterval[0]):
            