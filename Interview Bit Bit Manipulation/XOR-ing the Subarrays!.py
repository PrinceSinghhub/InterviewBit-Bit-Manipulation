class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        if len(A) % 2 == 0:
            return 0

        else:
            xorVal = A[0]
            for i in range(2, len(A), 2):
                xorVal ^= A[i]

            return xorVal

ans = Solution()
A = [1, 2, 3]
print(ans.solve(A))