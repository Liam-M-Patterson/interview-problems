class Solution:
    def merge(self, intervals):
        #sort
        intervals.sort(key = lambda i : i[0])
        
        res = []
        curr = intervals[0]
        
        for interval in intervals:
            
            #if overlaps, update curr
            if interval[0] >= curr[0] and interval[0] <= curr[1]:
                curr = [min(curr[0], interval[0]), max(curr[1], interval[1])]
            else: #not overlapping, insert curr, then update curr
                res.append(curr)
                curr = interval
        
        
        res.append(curr)
        return res