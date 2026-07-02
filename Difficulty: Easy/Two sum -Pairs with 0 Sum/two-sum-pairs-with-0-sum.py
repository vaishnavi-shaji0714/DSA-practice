class Solution:
    def getPairs(self, arr):
        arr.sort()
        n = len(arr)
        i = 0
        j = n-1
        target = 0
        res = []
        
        while i<j:
            s = arr[i] + arr[j]
            if s == target:
                res.append([arr[i], arr[j]])
                i += 1
                j -= 1
                while i < j and arr[i] == arr[i-1]:
                    i += 1
                while j == 0 and arr[j] == arr[j+1]:
                    j -= 1
            elif s < target:
                i += 1
            else:
                if s > target:
                    j -= 1
        return res