class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = 0
        high = 0
        s = 0
        res = float('inf')
        n = len(nums)
        while high<n:
            s = s + nums[high]
            while s >= target:
                length_of_arr = (high - low) + 1
                res = min(res,length_of_arr)
                s = s - nums[low]
                low += 1
            high += 1
        
        if res != float('inf'):
            return res
        else:
            return 0