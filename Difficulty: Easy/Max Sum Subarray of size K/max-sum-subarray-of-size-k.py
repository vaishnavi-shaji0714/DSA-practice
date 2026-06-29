class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        low = 0
        high = k-1
        n = len(arr)
        s = 0
        res = 0
        for i in range(high+1):
            s = s + arr[i]
            
        while high<n:
            res = max(res,s)
            low += 1
            high += 1
                
            s = s - arr[low-1]
            
            
            if high == n:
                break
            s = s + arr[high]
              
        return res