class Solution:
    def longestKSubstr(self, s, k):
        low = 0
        high = 0
        n = len(s)
        res = float("-inf")
        hm = {}
        for high in range(n):
            hm[s[high]] = hm.get(s[high],0) + 1
        
            while len(hm) > k:
                hm[s[low]] = hm.get(s[low]) - 1
                if hm[s[low]] == 0:
                    del hm[s[low]]
                low += 1
            if len(hm) == k:
                length = high - low + 1
                res = max(res,length)
        
        if res == float("-inf"):
            return -1
        else:
            return res
              