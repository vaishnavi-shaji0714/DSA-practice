class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        low = 0
        high = 0
        k = 2
        res = -1
        hm = {}
        n = len(fruits)
        for high in range(n):
            hm[fruits[high]] = hm.get(fruits[high], 0) + 1
            while len(hm) > k:
                hm[fruits[low]] = hm.get(fruits[low]) - 1
                if hm[fruits[low]] == 0:
                    del hm[fruits[low]]
                low += 1
            
            if len(hm) < k or len(hm)==k:
                length = high - low + 1
                res = max(res, length)

        return res