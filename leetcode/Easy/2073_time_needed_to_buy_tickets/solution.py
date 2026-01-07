# Solution for https://leetcode.com/problems/time-needed-to-buy-tickets/
# Other solutions: https://github.com/Melodiz/dailycode/tree/main/leetcode

from typing import List, Optional

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total_time = tickets[k]
        for i, x in enumerate(tickets):
            if i == k: continue
            elif i < k:
                total_time += min(x, tickets[k])
            else:
                total_time += min(x, tickets[k]-1)
        return total_time
