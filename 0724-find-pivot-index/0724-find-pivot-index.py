class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        totalsum = 0
        for i in range(n):
            totalsum = totalsum + nums[i]
        
        if totalsum - nums[0] == 0:
            return 0
        
        for j in range(1,n):
            left = left + nums[j-1]
            right = totalsum - left - nums[j]
            if left == right:
                return j
        
        return -1