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
                    miss = arr[i]
                else:
                    occurs = arr[i]

        return [occurs, miss]
        
