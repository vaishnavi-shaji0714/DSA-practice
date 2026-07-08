class Solution:
    def smallestSumSubarray(self, A, N):
        best_ending = A[0]
        ans = A[0]
        n = len(A)
        for i in range(1,n):
            v1 = best_ending + A[i]
            v2 = A[i]
            best_ending = min(v1, v2)
            ans = min(best_ending, ans)
        return ans