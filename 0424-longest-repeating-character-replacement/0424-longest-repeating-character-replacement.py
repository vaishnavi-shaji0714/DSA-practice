class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        low = 0
        high = 0
        res = 0
        n = len(s)
        hm = {}
        max_freq = 0
        for high in range(n):
            hm[s[high]] = hm.get(s[high], 0) + 1
            max_freq = max(max_freq,hm[s[high]])
            length = high - low + 1
            diff = length - max_freq
            while diff > k:
                hm[s[low]] = hm.get(s[low]) - 1
                low += 1
                length = high - low + 1
                diff = length - max_freq
            
            res = max(res, length)

        return res