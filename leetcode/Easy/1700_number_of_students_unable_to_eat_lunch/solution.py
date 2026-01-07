# Solution for https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
# Other solutions: https://github.com/Melodiz/dailycode/tree/main/leetcode

from typing import List, Optional


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = [len(students)-sum(students), sum(students)]
        for x in sandwiches:
            if count[x] == 0: break
            count[x]-=1
        return sum(count)