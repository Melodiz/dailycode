# Solution for https://leetcode.com/problems/apple-redistribution-into-boxes/
# Other solutions: https://github.com/Melodiz/dailycode/tree/main/leetcode

from typing import List, Optional

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        req = sum(apple)
        for i, v in enumerate(capacity):
            if v >= req: return i + 1
            req -= v
        return -1


if __name__ == "__main__":
    Solution.minimumBoxes()
