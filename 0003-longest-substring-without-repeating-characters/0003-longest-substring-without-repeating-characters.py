class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low = 0
        high = 0
        n = len(s)
        res = 0
        hm = {}
        for high in range(n):
            hm[s[high]] = hm.get(s[high],0) + 1
            k = high - low + 1
            while len(hm) < k:
                hm[s[low]] = hm.get(s[low]) - 1
                if hm[s[low]] == 0:
                    del hm[s[low]]
                low += 1
                k = high - low + 1
            if len(hm) == k:
                length = high - low + 1
                res = max(res,length)
        return res
