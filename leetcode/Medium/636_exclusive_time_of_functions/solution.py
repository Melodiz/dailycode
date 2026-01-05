# Solution for https://leetcode.com/problems/exclusive-time-of-functions/
# Other solutions: https://github.com/Melodiz/dailycode/tree/main/leetcode

from typing import List, Optional

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n
        stack = []
        
        for log in logs:
            fid, event, time = log.split(":")
            fid = int(fid)
            time = int(time)
            
            if event == "start":
                if stack:
                    prev_fid, prev_start = stack[-1]
                    result[prev_fid] += time - prev_start
                stack.append([fid, time])
            else:
                curr_fid, curr_start = stack.pop()
                result[curr_fid] += time - curr_start + 1
                if stack:
                    stack[-1][1] = time + 1
        
        return result

