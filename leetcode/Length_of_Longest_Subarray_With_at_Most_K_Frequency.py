class Solution:
    def maxSubarrayLength(self, nums, k: int) -> int:
        ans = 0
        data = {}
        l = 0
        for r in range(len(nums)):
            data[nums[r]] = data.get(nums[r], 0) + 1
            if data[nums[r]] > k:
                while nums[l] != nums[r]:
                    data[nums[l]] -= 1
                    l += 1
                data[nums[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
