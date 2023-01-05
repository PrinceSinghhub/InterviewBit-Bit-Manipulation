class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):

        A.sort()
        minXOR = float("inf")

        for i in range(len(A) - 1):
            if A[i] ^ A[i+1] < minXOR:
                minXOR = A[i] ^ A[i+1]
        return minXOR

        # bruteforce Approvh
        # A.sort()

        # Min = float('inf')
        # for i in range(len(A) - 1):
        #     for j in range(i + 1, len(A)):
        #
        #         xor = A[i] ^ A[j]
        #         if xor <= Min:
        #             Min = xor
        #
        # return Min


ans = Solution()
arr = [ 3, 2, 13, 1, 5, 13, 0, 13, 13 ]
print(ans.findMinXor(arr))
