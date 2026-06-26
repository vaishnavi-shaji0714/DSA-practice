class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        posarr = []
        negarr = []
        res = []
        for i in range(len(nums)):
            if nums[i] >= 0:
                posarr.append(nums[i])
            else:
                negarr.append(nums[i])
        
        n = len(posarr)
        m = len(negarr)

        if n == 0:
            for i in range(m):
                negarr[i] = negarr[i] * negarr[i]
            negarr.reverse()
            return negarr
        if m == 0:
            for i in range(n):
                posarr[i] = posarr[i] * posarr[i]
            return posarr
        
        for i in range(m):
            negarr[i] = negarr[i] * negarr[i]
        negarr.reverse()
        for i in range(n):
            posarr[i] = posarr[i] * posarr[i]
        
           
        i = 0
        j = 0

        while i<n and j<m:
            if posarr[i] < negarr[j]:
                res.append(posarr[i])
                i += 1
            else:
                res.append(negarr[j])
                j += 1
        
        while i<n:
            res.append(posarr[i])
            i += 1
        while j<m:
            res.append(negarr[j])
            j += 1

        return res
