class Solution:
    def countTriplets(self, sum, arr):
        arr.sort()
        i = 0
        n = len(arr) 
        res = 0
        for i in range(n-2):
            
        
            j = i + 1
            k = n - 1

            while j<k:
                s = arr[i] + arr[j] + arr[k]
                if s >= sum:
                    
                    k -= 1

                    
                
                else:
                    res = res + (k-j)
                    j += 1
        
        return res