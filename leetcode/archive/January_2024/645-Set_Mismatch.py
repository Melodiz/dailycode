class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        arr = [0 for x in range(n+1)]
        for x in nums:
            arr[x] +=1
        miss = 0
        occurs = 0
        for i in range(1, n+1):
            if arr[i] != 1:
                if arr[i] == 0:
                    miss = i
                else:
                    occurs = i
        return [occurs, miss]
        


# nums = [2, 3, 3, 4, 5, 6]
# print(Solution.findErrorNums(Solution, nums))
