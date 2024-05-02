class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        max_k = float('-inf')
        while left < right:
            if nums[left] + nums[right] == 0:
                max_k = max(max_k, nums[right])
                left += 1
                right -= 1
            elif nums[left] + nums[right] < 0:
                left += 1
            else:
                right -= 1
        return max_k if max_k != float('-inf') else -1  # If no such pair found