class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        i = 0
        n = len(nums) 
        res = []
        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
        
            j = i + 1
            k = n - 1
            sum = -1*nums[i]

            while j<k:
                s = nums[j] + nums[k]
                if s == sum:
                    
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j<n and nums[j] == nums[j-1]:
                        j += 1
                        
                    while k>=0 and nums[k] == nums[k+1]:
                        k -= 1
                
                elif s<sum:
                    j += 1
                else:
                    k -= 1
        
        return res