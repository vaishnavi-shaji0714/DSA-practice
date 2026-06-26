class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        result = 1
        k = 1
        while (k<len(nums)):
            if (nums[k] == nums[k-1]):
                k += 1
                continue
            nums[i+1] = nums[k]
            i += 1
            result += 1
            k += 1
        return result