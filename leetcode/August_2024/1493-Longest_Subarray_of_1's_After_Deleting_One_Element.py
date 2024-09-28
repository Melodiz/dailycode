class Solution:
    def longestSubarray(self, nums) -> int:
        max_ans = 0
        l, r = 0, 0
        last_zero = -1
        isZero = False
        while r < len(nums):
            if nums[r] == 0:
                if not isZero:
                    last_zero = r
                    isZero = True
                else:
                    max_ans = max(max_ans, r - l - 1)
                    l = last_zero + 1
                    last_zero = r
            r += 1
        max_ans = max(max_ans, r - l - 1)
        return max_ans