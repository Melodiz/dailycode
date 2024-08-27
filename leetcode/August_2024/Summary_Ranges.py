class Solution:
    def summaryRanges(self, nums):
        if len(nums) == 0: return []
        start = nums[0]
        last_num = nums[0]
        ans = []
        for num in nums[1:]:
            if num == last_num + 1:
                last_num = num
            else:
                ans.append(f"{start}->{last_num}" if start!= last_num else str(start))
                start = num
                last_num = num
        ans.append(f"{start}->{last_num}" if start!= last_num else str(start))
        return ans

