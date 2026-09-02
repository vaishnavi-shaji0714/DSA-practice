class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        totalsum = 0
        hashmap = {0:1}
        n = len(nums)
        res = 0
        
        for i in range(n):
            totalsum = totalsum + nums[i]
            ques = totalsum - k
            freq = hashmap.get(ques,0)
            res = res + freq
            hashmap[totalsum] = hashmap.get(totalsum,0) + 1
        return res      